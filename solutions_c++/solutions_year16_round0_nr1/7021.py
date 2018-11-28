#include<bits/stdc++.h>
#define M 1000000
#define ll long long int
using namespace std;
ll findLastNum(ll n){
	bool b[10]={false};
	ll i,j,k,m,z,ret=-1;
	for(i=1;;i++){
		if(i>M){
			break;
		}
		m=i*n;
		z=m;
		while(m>0){
			b[m%10]=true;
			m=m/10;
		}
		k=0;
		for(j=0;j<10;j++){
			if(b[j])
				k++;
		}
		if(k==10){
			ret=z;
			break;
		}
	}
	return ret;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large-output.out","w",stdout);
	
	ll i,j,k,n,t,ans;
	cin>>t;
	for(i=1;i<=t;i++){
		cin>>n;
		if(n==0){
			printf("Case #%lld: INSOMNIA\n",i);		
		}
		else{
			ans=findLastNum(n);
			if(ans==-1){
				printf("Case #%lld: INSOMNIA\n",i);
			}
			else{
				printf("Case #%lld: %lld\n",i,ans);
			}
		}	
	}
	return 0;
}
