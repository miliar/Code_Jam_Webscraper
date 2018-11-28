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

int T,n,m;
int dig[N],fac[N];

int main() {
	if(DEBUG){
		freopen("in.in","r",stdin);
		freopen("out.out","w",stdout);
	}
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
    	printf("Case #%d:\n",t);
    	scanf("%d%d",&n,&m);
    	memset(dig,0,sizeof(dig));
    	dig[0]=dig[n-1]=1;
    	for(int i=0;m;i++){
	    	for(int j=n-2,k=i;j>0;j--,k/=2){
	    		dig[j]=k%2;
	    	}
	    	int flag=1;
	    	for(int j=2;j<=10;j++){
	    		LL tmp=0;
	    		for(int k=0;k<n;k++){
		    		tmp=tmp*j+dig[k];
		    	}
		    	int tmpflag=0;
		    	for(int k=sqrt(tmp);k>=2;k--){
	    			if(tmp%k==0){
			    		tmpflag=1;
			    		fac[j]=k;
			    		break;
			    	}
	    		}
	    		if(!tmpflag){
		    		flag=0;
		    		break;
		    	}
	    	}
	    	if(flag){
	    		m--;
	    		for(int j=0;j<n;j++){
		    		printf("%d",dig[j]);
		    	}
		    	for(int j=2;j<=10;j++){
	    			printf(" %d",fac[j]);
	    		}
	    		printf("\n");
	    	}
	    }
    }
    return 0;
}
