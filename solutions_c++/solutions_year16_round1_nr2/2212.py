#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef vector <int>    VI;
typedef pair <int,int > PII;
#define FOR(i,x,y)  for(int i = x;i < y;++ i)
#define IFOR(i,x,y) for(int i = x;i > y;-- i)
#define pb  push_back
#define mp  make_pair
#define fi  first
#define se  second

const int maxn = 3000;
int n,cnt[maxn];

int main(){
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    int T,tCase = 0;    scanf("%d",&T);
    while(T--){
        printf("Case #%d:",++tCase);
        scanf("%d",&n);
        FOR(i,0,maxn)   cnt[i] = 0;
        int num;
        FOR(i,0,2*n-1)  FOR(j,0,n)  scanf("%d",&num),cnt[num]++;
        bool f = false;
        FOR(i,0,maxn){
            if(cnt[i]%2)
                printf(" %d",i);
        }
        printf("\n");
    }
    return 0;
}

