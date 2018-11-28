

#include <iostream>
#include <stdio.h>
#include <string>
#include <map>

using namespace std;
int data[100];
int n;
int make[100];
int visit[100];
int maxx = 0;
int v2[100];


void dfs(int len)
{
    int check = 0;
    for(int i=1;i<=len;i++)
    {
        int next = i+1;
        if(next == len+1)next = 1;
        int pre = i-1;
        if(pre == 0)pre= n;
        if(data[make[i]]!=make[next] && data[make[i]]!=make[pre])
        {
            check=1;
            break;
        }
    }
    if(check == 0)
    {
        if(len>maxx)maxx = len;
    }
    for(int i=1;i<=n;i++)
    {
        if(visit[i] == 0)
        {
            visit[i] = 1;
            make[len+1] = i;
            dfs(len+1);
            visit[i] = 0;
            make[len+1] = 0;
        }
    }
}



int main(int argc, const char * argv[]) {
   freopen("/Users/sangwoo/Desktop/cpp/cpp/input","r",stdin);
   freopen("/Users/sangwoo/Desktop/cpp/cpp/output","w",stdout);
    
    int tt;
    
    cin >> tt;
    
    for(int i=1;i<=tt;i++)
    {
        maxx=0;
        scanf("%d",&n);
        for(int j=1;j<=n;j++)
        {
            scanf("%d",&data[j]);
        }
        
        dfs(0);
        
        printf("Case #%d: %d\n",i,maxx);
        
    }
    

    return 0;
}