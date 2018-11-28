#include<bits/stdc++.h>
#define x first
#define y second
using namespace std;
int t,n,m;
char s[1005];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&t);
	for(int _=1;_<=t;++_){
		scanf("%s%d",s,&m);
		n=strlen(s);
		for(int i=0;s[i];++i){
			if(s[i]=='+')s[i]=0;
			else s[i]=1;
		}
		bool is=0;
		int ans=0;
		for(int i=0;i<n;++i){
			if(s[i]){
				if(i+m>n){
					is=1;
					break;
				}
				for(int j=0;j<m;++j){
					s[i+j]^=1; 
				}
				++ans;
			}
			//for(int j=0;j<n;++j)putchar(s[j]?'1':'0');puts("");
		}
		printf("Case #%d: ",_);
		if(is)puts("IMPOSSIBLE");
		else printf("%d\n",ans);
	}
	return 0;
}

