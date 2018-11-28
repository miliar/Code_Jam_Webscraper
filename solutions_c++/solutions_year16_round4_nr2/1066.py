#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<iomanip>
using namespace std;
long double p[300];
int n;
int k;
long double rec(vector<long double> a,int r,int id){
	//for(int i=0;i<a.size();++i)
	//	cout<<a[i]<<" ";
	//cout<<endl;
	if(r==0){
		return a[k/2];
	}
	if(id>=n){
		return 0;
	}
	long double tmp = rec(a,r,id+1);
	int last = a.size()-1;
	a.push_back(a[last]*p[id]);
	for(int i=last;i>=0;--i){
		a[i]=a[i]*(1-p[id]);
		if(i>=1)
			a[i]+=a[i-1]*p[id];
	}
	long double tmp2 = rec(a,r-1,id+1);
	if(tmp2>tmp)
		return tmp2;
	else
		return tmp;
}
int main(){
	int TT;
	cin>>TT;
	long double ans=0;
	long double a[300];
	for(int T=1;T<=TT;++T){
		cin>>n>>k;
		for(int i=0;i<n;++i)
			cin>>p[i];
		vector<long double> v;
		v.push_back(1);
		ans = rec(v,k,0);

		cout<<fixed<<setprecision(9)<<"Case #"<<T<<": "<<ans<<"\n";
	}
	return 0;
}

