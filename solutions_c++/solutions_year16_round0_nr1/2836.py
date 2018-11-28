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

int T,n,num,ans;
int flag[N];

int main() {
	if(DEBUG){
		freopen("in.in","r",stdin);
		freopen("out.out","w",stdout);
	}
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
    	scanf("%d",&n);
    	if(!n){
	    	printf("Case #%d: INSOMNIA\n",t);
	    	continue;
	    }
    	memset(flag,0,sizeof(flag));
    	num=0;
    	for(int i=1;i<100;i++){
	    	int k=i*n;
	    	while(k){
	    		int j=k%10;
	    		if(!flag[j]){
		    		flag[j]=1;
		    		num++;
		    	}
	    		k/=10;
	    	}
	    	if(num==10){
	    		ans=i*n;
	    		break;
	    	}
	    }
	    printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
