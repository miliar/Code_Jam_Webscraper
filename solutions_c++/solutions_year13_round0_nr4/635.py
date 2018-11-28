#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <math.h>
#include <map>
#include <vector>

using namespace std;

int K,N;
int Ans[200];
int keys[200+1];
int keys_total[200+1];
int Ti[200];
int Kn[200];
int Ka[200][400];

map<vector<int>,int> result_map;

int search(int *opened,int level)
{
	int i;
	/*fprintf(stderr,"level=%d ",level);
	for (i=0;i<N;i++){
		fprintf(stderr," %d",Ans[i]+1);
	}
	fprintf(stderr,"\n");*/
	vector<int> opened_v;
	for (i=0;i<N;i++){
		opened_v.push_back(opened[i]);
	}
	//全部開けたら終了
	if (level==N)return 1;
	//枝刈り:できない組み合わせになったら抜ける
	if (result_map.find(opened_v)!=result_map.end())return 0;
	//枝刈り:残った鍵の合計で開けられないものがひとつでもあればあきらめる
	for (i=0;i<N;i++){
		if (!opened[i]){
			if (keys_total[Ti[i]]<1){
				result_map[opened_v]=0;//できない組み合わせを追加
				return 0;
			}
		}
	}
	//開けられるものから小さい順にトライ
	for (i=0;i<N;i++){
		if ( (!opened[i]) && (keys[Ti[i]]>=1) ){
			//開けられる。トライ
			//フラグ設定
			opened[i]=1;
			//鍵を減らす
			keys[Ti[i]]--;
			keys_total[Ti[i]]--;
			//入っていた鍵を加算
			int j;
			for (j=0;j<Kn[i];j++){
				keys[Ka[i][j]]++;
			}
			//ルート記述
			Ans[level]=i;
			if (search(opened,level+1)==1)return 1;
			//元に戻す
			opened[i]=0;
			keys[Ti[i]]++;
			keys_total[Ti[i]]++;
			for (j=0;j<Kn[i];j++){
				keys[Ka[i][j]]--;
			}
		}
	}
	result_map[opened_v]=0;//できない組み合わせを追加
	return 0;
}

int main(int argc,char **argv)
{
	int t,T;
	int i,j;
	scanf("%d\n",&T);
	for (t=1;t<=T;t++){
		scanf("%d %d\n",&K,&N);
		memset(keys,0,sizeof(keys));
		memset(keys_total,0,sizeof(keys_total));
		result_map.clear();
		for (i=0;i<N;i++){
			Ans[i]=-1;
		}
		for (i=0;i<K;i++){
			int k;
			scanf("%d ",&k);
			keys[k]++;
			keys_total[k]++;
		}
		for (i=0;i<N;i++){
			scanf("%d %d ",&Ti[i],&Kn[i]);
			for (j=0;j<Kn[i];j++){
				scanf("%d ",&Ka[i][j]);
				keys_total[Ka[i][j]]++;
			}
		}
		int opened[N];
		memset(opened,0,sizeof(opened));
		int ret=search(opened,0);
		printf("Case #%d:",t);
		if (ret==0)printf(" IMPOSSIBLE\n");
		else{
			for (i=0;i<N;i++){
				printf(" %d",Ans[i]+1);
			}
			printf("\n");
		}
	}
	return 0;
}
