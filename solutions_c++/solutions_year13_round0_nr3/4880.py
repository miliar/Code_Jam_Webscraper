#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<map>
#include<set>
#include<queue>
#include<vector>
#include<cmath>

using namespace std;

#define FOR(i,n,first) for(int i=first;i<n;i++)
#define lson l , m , rt << 1
#define rson m + 1 , r , rt << 1 | 1
#define pb push_back
#define N 110
#define M 101000
const int MOD=100000007;
const int INF = 0x3f3f3f3f;
typedef long long int Int64;
//#define SMALL


int maps[N][N];

/*bool pali(int x){
	int que[100];
	int top=0;
	while(x){
		que[top++]=x%10;
		x/=10;
	}
	for(int i=0;i<top;i++)
}

bool judge(int x){
	if(!pali(x))return false;
	int y=sqrt(x);
	if(y*y==x){
		if(pali(y))return true;
		else return false;
	}
	return false;
}

void init(){
	for(int i=1;i<=1000;i++){
		if(judge(i)){
			printf("pal=%d\n",i);
		}
	}
}*/

bool judge(int x){
	int y=sqrt(x);
	if(y*y==x){
		return true;
		
	}
	return false;
}
int a[1100];//={1,4,9,121,484};

int main()
{
	#ifdef SMALL
    freopen("C-small-attempt0.in","rt",stdin);
    freopen("text.out","w",stdout);
    #endif
    int cas,aa,bb;
    scanf("%d",&cas);
    memset(a,0,sizeof a);
    a[1]=a[4]=a[9]=a[121]=a[484]=1;
    for(int ii=1;ii<=cas;ii++){
    	scanf("%d%d",&aa,&bb);
    	int ans=0;
    	for(int i=aa;i<=bb;i++)
    		ans+=a[i];
    	printf("Case #%d: %d\n",ii,ans);
    }
    return 0;
}