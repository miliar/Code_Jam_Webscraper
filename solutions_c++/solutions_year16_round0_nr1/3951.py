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
int t,m,q,k,ans,cs=0;
int a[N],b[N];
set<int> S;
int main(){
    scanf("%d",&t);
    while(t--){
        LL lst=0,n;
        scanf("%lld",&n);
        S.clear();
        int i=0,newdigit=0;
        if(n>0)do{
            //printf("lst:%lld\n",lst);
            lst = n*(LL)(++i);
            newdigit=0;
            LL tmp = lst;
            do{
                int dg=tmp%10;
                if(S.count(dg)==0){
                    ++newdigit;
                    S.insert(dg);
                }
                tmp/=10;
            }while(tmp>0);
            if(S.size()==10)break;
        }while(true);
        printf("Case #%d: ",++cs);
        if(n>0 && S.size()==10)printf("%lld\n",lst);
        else printf("INSOMNIA\n");
    }
	return 0;
}

