#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char visit[1<<22];
int keys[201];
int kpt;
typedef struct { int k; int cap; int con[201]; int open;} chest_t;
chest_t chests[201];
int cpt;
int result[201];
inline int getid(int dep){
	int res=0;
	for(int i=0;i<dep;i++)
		res+= 1<<result[i];
	return res;
}
int solve(int dep){
	////
	//for(int i=0;i<dep;i++)
	//	printf("  ");
	//for(int i=0;i<200;i++)
	//	if(keys[i]!=0)
	//		printf("(%d,%d)",i,keys[i]);
	//if(dep)
	//{
	//	printf("open %d ",result[dep-1]);
	//	int yyyy= result[dep-1];
	//	for(int i=0;i<chests[yyyy].cap;i++)
	//		printf("%d ",chests[yyyy].con[i]);
	//}
	//printf("\n");
	//
	if(dep==cpt)
		return true;
	int id=getid(dep);
	if(visit[id])
		return false;
	visit[id]=1;
	for(int i=0;i<cpt;i++){
		if( (!chests[i].open) && keys[chests[i].k]!=0){
			//open
			result[dep]=i;
			chests[i].open=1;
			for(int j=0;j<chests[i].cap;j++){
				keys[chests[i].con[j]]++;
			}
			keys[chests[i].k]--;
			//calc
			if(solve(dep+1))
				return true;
			//close
			chests[i].open=0;
			for(int j=0;j<chests[i].cap;j++){
				keys[chests[i].con[j]]--;
			}
			keys[chests[i].k]++;
		}
	}
	return false;
}
int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		memset(keys,0,sizeof(keys));
		memset(chests,0,sizeof(chests));
		memset(visit,0,sizeof(visit));
		scanf("%d%d",&kpt,&cpt);
		for(int i=0;i<kpt;i++){
			int tmp;
			scanf("%d",&tmp);
			keys[tmp]++;
		}
		for(int i=0;i<cpt;i++){
			int t1,t2;
			scanf("%d",&(chests[i].k));
			scanf("%d",&t1);
			chests[i].cap=t1;
			for(int j=0;j<t1;j++){
				scanf("%d",&t2);
				chests[i].con[j]=t2;
			}
		}
		printf("Case #%d: ",t);
		if(solve(0)){
			for(int i=0;i<cpt;i++){
				printf("%d ",result[i]+1);
			}
			puts("");
		}
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}