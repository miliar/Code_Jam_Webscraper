#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>
#include<map>
#include<set>
#include<vector>
#include<queue>
#include<cstdlib>
#include<ctime>
#include<cmath>
using namespace std;
typedef __int64 LL;
#define mod 1000000007
#define N 20
#define DEBUG 1

int T,k,c,s;

int main() {
	if(DEBUG){
		freopen("in.in","r",stdin);
		freopen("out.out","w",stdout);
	}
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
    	scanf("%d%d%d",&k,&c,&s);
    	printf("Case #%d:",t);
    	for(int j=1;j<=k;j++) printf(" %d",j);
    	printf("\n");
    }
    return 0;
}
