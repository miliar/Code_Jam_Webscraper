#include <iostream>
#include <vector>
using namespace std;

struct quart{
	int val;
	int sign;
};

quart neg(quart x){
	quart ans;
	ans.val= x.val;
	ans.sign= 0-x.sign;
	return ans;
}
	//1-> 1
	//2-> i
	//3-> j
	//4-> k
quart i, j, k, one;
void init(){
	i.val= 2;
	i.sign= 1;
	j.val= 3;
	j.sign= 1;
	k.val= 4;
	k.sign= 1;
	one.val= 1;
	one.sign= 1;
}

quart mul(quart a, quart b){
	if (a.sign>0 and b.sign<0){
		return neg(mul(a, neg(b)));
	}
	if (a.sign<0 and b.sign>0){
		return neg(mul(neg(a), b));
	}
	if (a.sign<0 and b.sign<0){
		return mul(neg(a), neg(b));
	}
	quart ans;
	int x= a.val, y= b.val;
	if (x==1){
		return b;
	}
	if (y==1){
		return a;
	}
	if (x==2 and y==2){
		return neg(one);
	}
	if (x==2 and y==3){
		return k;
	}
	if (x==2 and y==4){
		return neg(j);
	}
	if (x==3 and y==2){
		return neg(k);
	}
	if (x==3 and y==3){
		return neg(one);
	}
	if (x==3 and y==4){
		return i;
	}
	if (x==4 and y==2){
		return j;
	}
	if (x==4 and y==3){
		return neg(i);
	}
	if (x==4 and y==4){
		return neg(one);
	}
	
	
}

int main() {
	init();
	int t;
	cin>>t;
	for (int dhurr= 1; dhurr<=t; dhurr++){
		vector <quart> v;
		int l, x;
		cin>>l;
		cin>>x;
		char c[l];
		for (int ok=0; ok<l; ok++){
			cin>>c[ok];
		}
		vector <int> is, ik;
		quart well= one;
		for (int oh= 0; oh<x; oh++){
			for (int ok= 0; ok<l; ok++){
				if (c[ok]=='i'){
					v.push_back(i);
				}
				if (c[ok]=='j'){
					v.push_back(j);
				}
				if (c[ok]=='k'){
					v.push_back(k);
				}
			
			}
		}
		int n= l*x;
		for (int p= 0; p<n; p++){
		//	cout<<"("<<well.val<<", "<<well.sign<<") ("<<v[p].val<<", "<<v[p].sign<<") ";
			well= mul(well, v[p]);
		//	cout<<" "<<well.val<<" "<<well.sign<<endl;
			if (well.val==2 and well.sign>0){
				is.push_back(p);
			}
			if (well.val==4 and well.sign>0){
				ik.push_back(p);
			}
		}
	//	cout<<endl;
		if (ik.size()>0 and is.size()>0){
			if (is[0]<ik[ik.size()-1] and well.sign==-1 and well.val==1){
				cout<<"Case #"<<dhurr<<": YES"<<endl;
			}
			else{
				cout<<"Case #"<<dhurr<<": NO"<<endl;
			//	cout<<"not that much fucked up"<<endl;
			}
		}
		else{
		cout<<"Case #"<<dhurr<<": NO"<<endl;
		//	cout<<"too much fucked up"<<endl;
		}
	}
	return 0;
}