#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#include <map>
#include <string>

using namespace std;

// ある位置xの裏面にあるパンケーキを表にするのに必要な操作は、
// 1. 最上部のケーキが表なら裏返す
// 2. xまでをまとめて裏返す
// なので1か2ステップ。ケーキ枚数の最大値が100なので最大200ステップ以内には終わる
// 再帰で探索するとスタック消費量は200*101、だいたい20kB

// ある状態から終局までのステップ数をメモ化して探索数を減らせばいいかな

// 証明は思いつかないが、下のほうの連続している表向きパンケーキには触れないでも最短経路は変わらないと想定

map<string,int> cost_to_goal;
map<string,int> cost_from_start;

void flip(char *dest,char *src, int N)
{
	strcpy(dest,src);
	for (int i=0;i<N;i++){
		if (src[N-1-i]=='+'){
			dest[i]='-';
		}
		else if (src[N-1-i]=='-'){
			dest[i]='+';
		}
		else assert(0);
	}
	//strcpy(dest+N,src+N);
	//printf("%d %s -> %s\n",N,src,dest);
}

int states = 0;
int max_step = 0;

int search(char *S, int len, int step, int limit)
{
	states++;
	if (step>max_step)max_step=step;
	if (step > limit) return -1;
	//printf("%s %d %d\n",S,len,step);
	// 全部表なら終了
	if (len == 0)return 0;
	assert(S[len-1]=='-');
	string key(S);
	// もっと安いコストで来られるならそれ以上の探索を行う必要はない
	if (cost_from_start.find(key)!=cost_from_start.end()){
		if (cost_from_start[key]<=step)
			return -1;
	}
	/*if (cost_to_goal.find(key)!=cost_to_goal.end()){
		// メモ化対象に引っかかったのなら終了
		return cost_to_goal[key];
	}*/
	cost_from_start[key]=step;
	// lenまでの反転操作を全部試す
	int min_ret = -1;
	len = strlen(S);
	for (int i=1;i<=len;i++){
		char S_[101];
		int len_=len;
		flip(S_,S,i);
		while (len_>0){
			char c = S_[len_-1];
			if (c=='-')break;
			else if (c=='+'){
				len_--;
			}
			else assert(0);
		}
		// 再帰する
		int ret = search(S_,len_,step+1,limit);
		if (ret >= 0){
			if (min_ret < 0 || ret < min_ret){
				min_ret = ret;
			}
		}
	}
	//assert(cost_to_goal.find(key)==cost_to_goal.end());
	if (min_ret<0)return -1;
	cost_to_goal[key]=min_ret+1;
	return min_ret + 1;
}

int main(int argc,char **argv)
{
	int T;
	scanf("%d\n",&T);
	for (int t=1;t<=T;t++){
		char S[101];
		scanf("%s\n",S);
		int len = strlen(S);
		cost_to_goal.clear();
		cost_from_start.clear();
		//printf("%s\n",S);
		while (len>0){
			char c = S[len-1];
			if (c=='-')break;
			else if (c=='+'){
				len--;
			}
			else assert(0);
		}
		states = 0; max_step = 0;
		printf("Case #%d: %d\n",t,search(S,len,0,strlen(S)*2));
		// printf("states = %d, max_step = %d\n",states,max_step);
	}
	return 0;
}
