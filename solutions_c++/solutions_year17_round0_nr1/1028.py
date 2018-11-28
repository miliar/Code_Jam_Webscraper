#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> PII;

#define MAX_N 1005

int T;
int K;
char s[MAX_N];

int main(){
	freopen("A-large.in","r",stdin);
	freopen("ans2.txt","w",stdout);

	scanf("%d",&T);

	for(int ts=1;ts<=T;++ts){
		scanf("%s",s);
		scanf("%d",&K);

		int len=strlen(s);
		int ans=0;
		for(int i=0;i<len;++i){
			if(i>=len-K+1)break;
			//printf("%d\n",i);
			if(s[i]=='+')continue;
			++ans;
			for(int j=i;j<=i+K-1;++j){
				if(s[j]=='+')s[j]='-';
				else if(s[j]=='-')s[j]='+';
			}
		}


		// check answer
		for(int i=0;i<len;++i){
			if(s[i]=='-')ans=-1;
		}
		if(ans==-1){
			printf("Case #%d: IMPOSSIBLE\n",ts);
		}
		else {
			printf("Case #%d: %d\n",ts,ans);
		}
	}


	fclose(stdin);
	fclose(stdout);

	return 0;
}
