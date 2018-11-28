#include<bits/stdc++.h>

using namespace std;

int main(){
	
	int t,len;
	char st[1005];
	//freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++){
		
		int prev=0;
		int pay=0;
		scanf("%d %s",&len,st);
		
		for(int x=0;x<=len;x++){
			int need=st[x]-'0';
			while(need--){
				if(prev<x){
					int mem=x-prev;
					pay+=mem;
					prev+=mem;
				} 
				prev++;
			}
		}
		printf("Case #%d: %d\n",tc ,pay);
	}
}
