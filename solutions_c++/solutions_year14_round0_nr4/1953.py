#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
using namespace std;

bool found1(double key,vector<double> a,int &l,int &h){
	if(l>h) return false;
	for(int i=l;i<=h;i++){
		if(key<a[i]){
			l=i+1;
			return true;
		}
	}
	return false;
}

bool found2(double key,vector<double> a,int &l,int &h){
	if(h<l) return false;
	//cout<<"k="<<key<<" v"<<a[h]<<endl;
	for(int i=h;i>=l;i--){
		if(key>a[i]){
			h=i-1;
			return true;
		}
	}
	return false;
}


int main()
{
	int t,l=1;
	scanf("%d",&t);
	while(t--){
		int n;
		
		vector<double> a,b;
		scanf("%d",&n);
		//cout<<"hi\n";
		for(int i=0;i<n;i++){
			double d;
			scanf("%lf",&d);
			a.push_back(d);	
		}
		for(int i=0;i<n;i++){
			double d;
			scanf("%lf",&d);
			b.push_back(d);	
		}

		sort(a.begin(),a.end());
		sort(b.begin(),b.end());
		int l1=0,h1=n-1,c1=0;
		for(int i=0;i<n;i++){
			bool p=found1(a[i],b,l1,h1);
			if(p==false){
				c1=n-i;
				break;
			}
		}
		int l2=0,h2=n-1,c2=0;
		for(int i=n-1;i>=0;i--){
			bool p=found2(a[i],b,l2,h2);
			
			if(p==false){
				break;
			}
			else c2++;
		}
		printf("Case #%d: %d %d\n",l,c2,c1);
		l++;
	}
	return 0;
}
