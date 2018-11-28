#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <assert.h>
#include <string>
#include <map>

using namespace std;

typedef struct{
	char *S[8];
	int m;
}str_grp;

int mk_trie(str_grp *s,int idx){
	int nodes=1;
	// prefixで分ける
	str_grp child[26];
	/*fprintf(stderr,"prefix:\"");
	int x;
	assert(s->m>0);
	for (x=0;x<idx;x++){
		fprintf(stderr,"%c",s->S[0][x]);
	}
	fprintf(stderr,"\"\n");*/
	memset(child,0,sizeof(child));
	int i;
	for (i=0;i<s->m;i++){
		char c=s->S[i][idx];
		if (!('A' <= c && c <= 'Z'))continue;
		child[c-'A'].S[child[c-'A'].m]=s->S[i];
		child[c-'A'].m++;
	}
	for (i=0;i<26;i++){
		if (child[i].m)
			nodes+=mk_trie(&child[i],idx+1);
	}
	return nodes;
}

int main(void)
{
	int t,T;
	scanf("%d\n",&T);
	for (t=1;t<=T;t++){
		int m,M,N;
		scanf("%d %d\n",&M,&N);
		str_grp S;
		char S_ptr[100][100];
		memset(S_ptr,0,sizeof(char[100][100]));
		for (m=0;m<M;m++){
			scanf("%s\n",S_ptr[m]);
			S.S[m]=S_ptr[m];
			//fprintf(stderr,"%s\n",S.S[m]);
		}
		S.m=M;
		//fprintf(stderr,"%d %d\n",M,N);
		//int n_orig=mk_trie(&S,0);
		int X=-1; long long Y;
		int asg[M];
		memset(asg,0,sizeof(asg));
		while (1){
			int i;
			// distribute
			str_grp Sg[N];
			memset(Sg,0,sizeof(Sg));
			for (i=0;i<M;i++){
				assert(0<=asg[i] && asg[i]<=N-1);
				str_grp *dest=&Sg[asg[i]];
				dest->S[dest->m]=S.S[i];
				dest->m++;
			}
			// sanity check
			int look=1;
			for (i=0;i<N;i++){
				if (Sg[i].m<=0)look=0;
			}
			if (look){
				int total_nodes=0;
				for (i=0;i<N;i++){
					total_nodes+=mk_trie(&Sg[i],0);
				}
				if (total_nodes>X){
					X=total_nodes;Y=1;
				}
				else if (total_nodes==X){
					Y++;
				}
			}
			// exit check
			int done=1;
			for (i=0;i<M;i++){
				if (asg[i]!=N-1)done=0;
			}
			if (done)break;
			int carry=1;
			// increment selection
			for (i=0;i<M;i++){
				if (carry){
					asg[i]++;
					if (asg[i]==N){
						asg[i]=0;
					}
					else carry=0;
				}
			}
		}
		printf("Case #%d: %d %d\n",t,X,(int)(Y % 1000000007));
	}
	return 0;
}
