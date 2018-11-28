#include "stdio.h"
#include "string.h"
#include <algorithm>
#include <queue>
#include <map>
#include <iostream>
#include <vector>
#include <string>
using namespace std;
int required[205];
int has[205][205];
int hasCnt[205];
int Ihas[205];
int K, N;
int opened[205];
bool includeSelf[205];
bool subset[100][100];
void Process(){
	int cnt[205];
	memset(subset,1,sizeof(subset));
	for(int i=0;i<N;i++){
		for(int j=i+1;j<N;j++){
			memset(cnt,0,sizeof(cnt));
			for(int k=0;k<hasCnt[i];k++)
				cnt[has[i][k]]++;
			cnt[required[i]]--;

			cnt[required[j]]++;
			for(int k=0;k<hasCnt[j];k++){
				cnt[has[j][k]]--;
				if(cnt[has[j][k]]<0){
					subset[i][j]=false;
				}
			}
			if(cnt[required[i]]<0)
				subset[i][j]=false;
		}
	}
}
bool Search(int cnt){
	if(cnt==N) return true;
	for(int i=0;i<N;i++){
		if(opened[i]!=-1) continue;
		if(Ihas[required[i]]==0) continue;

		/*bool thisissubset=false;
		for(int j=0;j<i;j++){
			if(opened[j]==-1&&subset[j][i]==true){
				thisissubset=true;
				break;
			}
		}
		if(thisissubset) 
			continue;*/

		Ihas[required[i]]--;
		for(int j=0;j<hasCnt[i];j++)
			Ihas[has[i][j]]++;
		opened[i]=cnt;

		if(Search(cnt+1)) return true;

		Ihas[required[i]]++;
		for(int j=0;j<hasCnt[i];j++)
			Ihas[has[i][j]]--;
		opened[i]=-1;

		if(includeSelf[i]) return false;
	}
	return false;
}
void Solve(){
	int cnt[205];
	memset(cnt,0,sizeof(cnt));
	memset(includeSelf,0,sizeof(includeSelf));
	scanf("%d %d",&K,&N);
	//printf("%d %d\n",K,N);
	memset(Ihas,0,sizeof(Ihas));
	for(int i=0;i<K;i++){
		int num;
		scanf("%d",&num);
		//printf("%d ",num);
		Ihas[num]++;
		cnt[num]++;
	}
	//printf("\n");
	for(int i=0;i<N;i++){
		scanf("%d",&required[i]);
		scanf("%d",&hasCnt[i]);
		cnt[required[i]]--;
		//printf("%d %d",required[i],hasCnt[i]);
		for(int j=0;j<hasCnt[i];j++){
			scanf("%d",&has[i][j]);
			if(has[i][j]==required[i])
				includeSelf[i]=true;
			//printf(" %d",has[i][j]);
			cnt[has[i][j]]++;
		}
		//printf("\n");
	}
	memset(opened,-1,sizeof(opened));
	for(int i=0;i<205;i++){
		if(cnt[i]<0){
			printf(" IMPOSSIBLE\n");
			return;
		}
	}
	//Process();
	if(Search(0)){
		for(int i=0;i<N;i++){
			for(int j=0;j<N;j++){
				if(opened[j]==i)
					printf(" %d",j+1);
			}
		}
		printf("\n");
	}
	else
		printf(" IMPOSSIBLE\n");
}
int main(){
	freopen("D:\\Test\\in.txt","r",stdin);
	freopen("D:\\Test\\out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){			
		printf("Case #%d:",t);
		Solve();
	}
    return 0;
}