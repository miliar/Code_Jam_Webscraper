#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef pair <int,int > PII;
#define FOR(i,x,y)  for(int i = x;i < y;++ i)
#define IFOR(i,x,y) for(int i = x;i > y;-- i)
#define pb  push_back
#define mp  make_pair
#define fi  first
#define se  second

const int maxn = 1010;
char a[maxn],b[maxn<<1];

void work(){
    int l = maxn,r = maxn-1;
    int len = strlen(a);
    b[++r] = a[0];
    FOR(i,1,len){
        if(a[i] >= b[l])    b[--l] = a[i];
        else    b[++r] = a[i];
    }
    FOR(i,l,r+1)    printf("%c",b[i]);
    printf("\n");
}

int main(){
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int T,tCase = 0;  scanf("%d",&T);
    while(T--){
        printf("Case #%d: ",++tCase);
        scanf("%s",a);
        work();
    }
    return 0;
}
