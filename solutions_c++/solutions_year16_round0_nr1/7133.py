#include<iostream>
#include<cstdio>
#define ll long long
using namespace std;
int main(){
	int t,n,flag;
	ll a,b[11];
	
	scanf("%d",&t);
	for(int tt=1;tt<=t;tt++){
		ll b[11]={0},val;
		
		scanf("%d",&n);	 flag=0;
		
		if(n==0) { printf("Case #%d: INSOMNIA\n",tt); continue; } 
		
		for(int i=0;i<101;i++){
			
			a=n*(i+1);
			int m=a;
			for(int k=m%10;m;m/=10,k=m%10) b[k]++;
			for(int j=0;j<10;j++){ if(!b[j]){ flag=0; break; } else flag=1; }
		    if(flag==1) { val=a; break; }
		}
		
		if(flag==1) printf("Case #%d: %lld\n",tt,val);
		
	}
	return 0;
}
