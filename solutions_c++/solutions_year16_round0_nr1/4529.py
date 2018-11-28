/*
 * Author:Õı”Ì«Ô(jywyq) 
 * Date:20160409
 */
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<string>
#include<cstring>
using namespace std;
#define LL long long
bool vis[10];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("dataout.txt","w",stdout);
	int t,n,cas=0;
	cin>>t;
	while(t--){
		memset(vis,0,sizeof vis);
		cin>>n;
		printf("Case #%d: ",++cas);
		if(n==0){
			puts("INSOMNIA");
			continue;
		}
		int k=1,N;bool ok=0;
		while(!ok){
			ok=1;
			N=k*n;
			while(N){
				vis[N%10]=1;
				N/=10;
			}
			for(int i=0;i<10;i++)if(!vis[i])ok=0;
			if(ok)break; 
			k++;
		}
		printf("%d\n",k*n);
		
		
		
	}
	
	
	
	
}
