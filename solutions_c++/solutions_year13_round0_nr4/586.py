#include <cstdio>
#include <cstring>
#include <cstdlib>

int originalKey,roomNumber;
int original[1000];
int insideNumber[100],inside[100][100],key[100];
int keyCnt[1<<20][25];
int memo[1<<20];

inline int dfs(int stat)
{
	if (stat==(1<<roomNumber)-1){
		return 1;
	}
	int &res=memo[stat];
	if (res!=-1){
		return res;
	}
	res=0;
	for (int i=0;i<roomNumber;++i){
		if (!(stat>>i&1) && keyCnt[stat][key[i]]>0){
			res|=dfs(stat|(1<<i));
		}
	}
	return res;
}

inline void output(int stat)
{
	if (stat==(1<<roomNumber)-1){
		return;
	}
	for (int i=0;i<roomNumber;++i){
		if (!(stat>>i&1) && keyCnt[stat][key[i]]>0 && dfs(stat|(1<<i))){
			printf(" %d",i+1);
			output(stat|(1<<i));
			return;
		}
	}
}

int main()
{
	int T,test=1;
	for (scanf("%d",&T);test<=T;++test){
		scanf("%d%d",&originalKey,&roomNumber);
		for (int i=0;i<originalKey;++i){
			scanf("%d",&original[i]);
		}
		
		for (int i=0;i<roomNumber;++i){
			scanf("%d%d",&key[i],&insideNumber[i]);
			for (int j=0;j<insideNumber[i];++j){
				scanf("%d",&inside[i][j]);
			}
		}
		
		for (int stat=0;stat<1<<roomNumber;++stat){
			memset(keyCnt[stat],0,sizeof(keyCnt[stat]));
			for (int i=0;i<originalKey;++i){
				++keyCnt[stat][original[i]];
			}
			for (int i=0;i<roomNumber;++i){
				if (stat>>i&1){
					--keyCnt[stat][key[i]];
					for (int j=0;j<insideNumber[i];++j){
						++keyCnt[stat][inside[i][j]];
					}
				}
			}
		}
		
		memset(memo,-1,sizeof(memo));
		if (!dfs(0)){
			printf("Case #%d: IMPOSSIBLE\n",test);
		}else{
			printf("Case #%d:",test);
			output(0);
			puts("");
		}
	}
	return 0;
}
