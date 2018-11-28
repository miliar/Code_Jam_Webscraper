#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <set>
#include <string>

using namespace std;

int N, M, sl[10];
char S[10][16];

int powd(int a, int b) {
	int ret=1;
	while (b--)
		ret*=a;
	return ret;
}

int main() {
	int T,Cas=0;
	scanf("%d",&T);
	while (T--) {
		scanf("%d%d",&M,&N);
		int hd=0, at=-1;
		for (int i=0;i<M;i++) {
			scanf("%s",S[i]);
			sl[i]=strlen(S[i]);
		}
		int top=powd(N,M);
		//static int sv[10][16], ln[10];
		//memset(ln,0,sizeof(ln));
		int best=-1, cnt=0;
		for (int i=0;i<top;i++) {
			int tmp=i;
			set<string> pref[6];
			for (int j=0;j<M;j++) {
				int x=tmp%N;
				for (int k=0;k<=sl[j];k++) {
					char bak=S[j][k];
					S[j][k]=0;
					pref[x].insert(S[j]);
					S[j][k]=bak;
				}
				//sv[x][ln[x]++]=j;
				tmp/=N;
			}
			int tot=0;
			for (int j=0;j<N;j++) {
				/*
				tmp=i;
				for (int k=0;k<M;k++) {
					int x=tmp%N;
					tmp/=N;
					if (x==j)
						printf("%s\t", S[k]);
				}
				printf(": ");
				for (set<string>::iterator it=pref[j].begin();it!=pref[j].end();++it)
					printf("%s ", it->c_str());*/
				//printf("%d ", pref[j].size());
				//printf("\n");
				tot+=pref[j].size();
			}
			//printf("============================\n");
			//printf("%d\n", tot);
			if (best<tot)
				best=tot, cnt=1;
			else if (best==tot)
				cnt++;
		}
		printf("Case #%d: %d %d\n",++Cas,best, cnt);
		fprintf(stderr, "%d\n", Cas);
		fflush(stderr);
	}
}

/*

1
4 2
AAA
AAB
AB
B

*/
