#include<iostream>
#include<fstream>
using namespace std;
#include<cmath>
#define max 6500005
bool prime[max]={0};

void seive(){
	prime[1]=1;
	for(int i=2;i<=sqrt(max);i++){
		if(prime[i]==0){
			for(int j=2*i;j<=max;j+=i){
				prime[j]=1;
			}
		}
	}
}

typedef long long ll;

int main(){
	ll t,i,j,k,x,l,n,d,flag,h;
	cin>>t;
	//seive();
	for(k=1;k<=t;++k){
		
		cin>>n>>h;
		cout<<"Case #"<<k<<":\n";
		
		ll a[n];
		
		a[n-1]=a[0]=1;
		
		x=pow(2,n-1);
		ll count=0;
		for(i=0;i<x;++i){
			l=i;
			for(j=1;j<=n-2;++j){
				if(l%2==1) a[j]=1;
				else a[j]=0;
				l/=2;
			}
			//for(j=n-1;j>=0;--j) cout<<a[j];
			//cout<<"\n";	
			ll flag=1;
			ll no[11];
			for(j=2;j<=10;++j){
				long long s=0,m=1;
				for(d=n-1;d>=0;--d){
					if(a[d]==1) s+=pow(j,d);
				}
				int p=0;
				for(d=2;d<=sqrt(s);++d){
					if(s%d==0){
						p=1;
						break;
					}
				}
				if(p==1) {
					no[j]=s;
					//cout<<j<<" "<<s<<"\n";
					//getchar();
				}else{ flag=0; break;}
				if(flag==0) break;
			}
			
			if(flag==1){
				//cout<<no[10]<<" ";
				for(j=n-1;j>=0;--j) cout<<a[j];
				cout<<" ";
				for(j=2;j<=10;++j){
					//cout<<j<<" "<<no[j]<<"\n";
					for(d=2;d<=sqrt(no[j]);++d){
						if(no[j]%d==0) {cout<<d<<" ";break;}
					}
				}
				cout<<"\n";
				count++;	
			}	
			if(count>=h) break;
			//for(j=1;j<=n-2;++j) a[j]=0;
		}	
	}
	return 0;
}
