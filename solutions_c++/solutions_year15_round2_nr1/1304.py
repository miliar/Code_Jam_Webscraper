#include <queue>
#include <stdio.h>
#include <algorithm>
#include <string.h>
using namespace std;
int next(int n){
	char s[100];
	sprintf(s,"%d",n);
	reverse(s,s+strlen(s));
	int nn;
	sscanf(s,"%d",&n);
	return n;
}
int dis[1000010];
int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		memset(dis,0x3f,sizeof(dis));
		int N;
		dis[1]=1;
		scanf("%d",&N);
		queue<int>q;
		q.push(1);
		while(!q.empty()){
			int t=q.front();
			if(t==N){
				break;
			}
			q.pop();
			if(dis[t+1]>dis[t]+1){
				dis[t+1]=dis[t]+1;
				q.push(t+1);
			}
			if(dis[next(t)]>dis[t]+1){
				dis[next(t)]=dis[t]+1;
				q.push(next(t));
			}
		}
		printf("%d\n",dis[N]);
	}
	return 0;
}
