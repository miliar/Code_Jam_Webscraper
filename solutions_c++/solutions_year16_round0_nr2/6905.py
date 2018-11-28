#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#define INF 0x3f3f3f3f
using namespace std;
long long readLong(){
    char c;
    long long n=0;
    c=getchar();
    while(c<'0'||c>'9')c=getchar();
    while(c>='0'&&c<='9'){
        n*=10;
        n+=(c-'0');
        c=getchar();
    }
    return n;
}

void dfs(char s[120], int n, int step, int &ret){
    int k = -1;
    bool yes = (s[0] == '+');
    for(int i=1; i<n; ++i){
        if(s[i] == '-'){
            yes = false;
        }
        if(s[i] != s[i-1]){
            k = i-1;
            break;
        }
    }
    if(yes){
        ret = min(ret, step);
        return;
    }
    if(k == -1)  k = n-1;
    for(int i=0; i<=k; ++i){
        s[i] = (s[i] == '+') ? '-':'+';
    }
    dfs(s,n,step+1,ret);
    return;
}

int main()
{
    freopen("B-large.in","r",stdin);
    //freopen("A-large-practice.in","r",stdin);
    freopen("b-large.out","w",stdout);
    int n,ret;
    char s[120];
    int T;
    scanf("%d",&T);
    int cas=0;
    while (T--)
    {
        scanf("%s",s);
        n = strlen(s);
        ret = INF;
        dfs(s,n,0,ret);
        printf("Case #%d: %d\n",++cas,ret);
    }
  return 0;
}
