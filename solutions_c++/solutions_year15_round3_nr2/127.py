#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>
//#include <math.h>
#include <algorithm>
using namespace std;

int k,l,s;
char kb[55];
char mo[55];
char exp[55];

int totapp=0,totseq=0,maxb=0;

void check(){
	totseq++;
	int cnt=0;
	for(int i=0;i+l<=s;i++){
		int flag=1;
		for(int j=0;j<l;j++)
			if(exp[j]!=mo[i+j]) flag=0;
		cnt+=flag;
	}
	totapp+=cnt;
	maxb=max(maxb,cnt);
}

void dfs(int dp){
	if(dp==s){
		check();
		return;
	}
	for(int i=0;i<k;i++){
		mo[dp]=kb[i];
		dfs(dp+1);
	}
}

int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("bsmall.txt","w",stdout);
	int T,Case=1;
	for(scanf("%d",&T);Case<=T;Case++){
		scanf("%d%d%d",&k,&l,&s);
		scanf("%s%s",kb,exp);
		totapp=totseq=maxb=0;
		dfs(0);
		//printf("%d %d\n",totapp,totseq);
		printf("Case #%d: %.8f\n",Case,(double)(maxb*totseq-totapp)/totseq);
	}
    return 0;
}

