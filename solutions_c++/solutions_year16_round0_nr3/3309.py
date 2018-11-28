#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <ctime>
#include <cmath>
using namespace std;
int s[90];
int n,k;
int id;
int T;
void dfs(int x)
{
    if(x == n-1)
    {
        for(int i=0;i<n;++i)printf("%d",s[i]);
        for(int i=2;i<=10;++i)printf(" %d",i+1);
        printf("\n");
        
        ++ id;
        if(id == k)exit(0);
        return;
    }
    
    if(x < n-3)
    {
        s[x] = s[x+1] = 1;
        dfs(x+2);
        s[x] = s[x+1] = 0;
    }
    dfs(x+1);
}
int main()
{
 //   freopen("C.out","w",stdout);
    scanf("%d",&T);
    scanf("%d%d",&n,&k);
    
    
    id = 0;
    memset(s,0,sizeof(s));
    s[0] = s[1] = s[n-2] = s[n-1] = 1;
    printf("Case #1:\n");
    dfs(2);
    
    //printf("%d\n",id);
    return 0;
    
}