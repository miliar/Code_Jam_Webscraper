#include<cstdio>
#include<cstring>
#include<bitset>
#include<stack>
#include<queue>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<iostream>
#include<cassert>
#include<climits>
#include<sstream>
#define N 111111
#define M 555555
#define LL long long
#define FOE(i,a,b) for(int i=(a);i<=(b);++i)
#define FOD(i,a,b) for(int i=(b);i>=(a);--i)
#define CLR(a,b) memset(a,b,sizeof(a))
#define lc(x) (x<<1)
#define rc(x) (lc(x)|1)
#define inf 0x3f3f3f3f
using namespace std;
int t,n,m,q,k,ans,cs=0;
int a[N],b[N];
char pk[222];
int main(){
    scanf("%d",&t);
    while(t--){
        scanf("%s",pk);
        int sl=strlen(pk);
        int flip=0,ct=0;
        for(int i=sl-1;i>=0;--i){
            int k = (pk[i]=='+')?1:0;
            k ^= flip;
            if(!k){
                ct++;
                flip^=1;
            }
        }
        printf("Case #%d: %d\n",++cs,ct);
    }
	return 0;
}

