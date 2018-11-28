#include <bits/stdc++.h>
using namespace std;
#define eprintf(...) fprintf(stderr,__VA_ARGS__)

const int N=12;

const char ord[]="RPS";

char s[N+1][3][(1<<N)+1],u[(1<<N)+1],v[(1<<N)+1];

int cnt[3];

int n,m,a[3];

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int T; scanf("%d",&T);
	for(m=0;m<3;m++)
		s[0][m][0]=ord[m];
	for(n=1;n<=12;n++)
		for(m=0;m<3;m++){
			strcpy(u,s[n-1][m]);
			strcat(u,s[n-1][(m+1)%3]);
			strcpy(v,s[n-1][(m+1)%3]);
			strcat(v,s[n-1][m]);
			if(strcmp(u,v)<0)
				strcpy(s[n][m],u);
			else
				strcpy(s[n][m],v);
		}
	for(int Case=1;Case<=T;Case++){
		scanf("%d%d%d%d",&n,&a[0],&a[1],&a[2]);
		v[0]=0;
		for(m=0;m<3;m++) if(a[m]){
			strcpy(u,s[n][m]);
			for(int i=0;i<3;i++) cnt[i]=0;
			for(char *c=u;*c;c++) cnt[*c=='R'?0:*c=='P'?1:2]++;
			bool ok=true;
			for(int i=0;i<3;i++) ok&=(cnt[i]==a[i]);
			if(!ok) continue;
			if(v[0]==0||strcmp(u,v)<0) strcpy(v,u);
		}
		printf("Case #%d: ",Case);
		puts(v[0]==0?"IMPOSSIBLE":v);
	}
}