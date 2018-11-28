#include<bits/stdc++.h>
#define ll long long
using namespace std;
bool check(int *a){
	bool f=1;
	for(int i=0;i<10;i++){
		if(a[i]==0){
			f=0;
			break;
		}
	}
	return f;
}
int main(){
	int t;
		ifstream fin("A-large.in");
	      ofstream fout("output.txt");
	fin>>t;
	for(int ii=1;ii<=t;ii++){
		int n;
		fin>>n;
		if(n==0){
			fout<<"Case #"<<ii<<": INSOMNIA"<<endl;

		}
		else{
		     vector<ll>v,d;
		int a[10]={0},i=2;
		ll s,r=n;
		while(r){
			v.push_back(r%10);
			a[r%10]=1;
			r=r/10;
		}
		ll rs;
		while(!check(a)){ ll rm=0;vector<ll>vr;
				    vr=v;
			for(int j=0;j<vr.size();j++){
					rs=vr[j]*i+rm;
					rm=rs/10;
					vr[j]=rs%10;
			}
			if(rm){
				   while(rm){
				   int rt;
				   rt=rm%10;
				   rm=rm/10;
				   vr.push_back(rt);
				   }
                  }
                  for(int i=0;i<vr.size();i++){
					a[vr[i]]=1;
				 }

                  i++;
                  d=vr;
		}
			fout<<"Case #"<<ii<<": ";
		for(int i=d.size()-1;i>=0;i--){
			fout<<d[i];
		}
		fout<<endl;
	}
      }
}
