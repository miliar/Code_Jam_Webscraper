#include<bits/stdc++.h>
#define ll long long 
using namespace std;
int check(int a[10]){
	int f=1;
	for(int i=0;i<=9;i++){
			if(a[i]!=1){
				f=0;break;
				}
			}
	return f;
}
int main(){
#ifndef ONLINE_JUDGE
    	freopen("input.in","r",stdin);
    	freopen("ou.txt","w",stdout);
    #endif
	int t,k=1;
	ll n,i,j,store;
	scanf("%d",&t);
	while(t--){
		int a[10]={0};
		i=1;
		scanf("%lld",&n);
		if(n==0){
			cout<<"Case #"<<k<<": INSOMNIA\n";
			}
	      else{
	         ll nn=n;
	         do{
		   nn=i*n;
		   store=nn;
		   while(nn){
		 	a[nn%10]=1;
			nn/=10;
			}
		    i++;
		    }while(!check(a));
		cout<<"Case #"<<k<<": "<<store<<endl;
		}
		k++;
	  }
return 0;
}
	
