#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

int J,N;
int T;
int s[50];

bool check(int n)
{
    for(int i=2;i<n;i++)
    {
        if(n%i == 0)
            return true;
    }
    return false;
}

bool judge(int n)
{
    int cnt;
    int Min = pow(n,0) + pow(n,N-1);
    int Max = 0;
    for(int i=0;i<N;i++)
    {
        Max += pow(n,i);
    }
    for(int i=Min;i<=Max;i++)
        if(!check(i));
            return false;
    return true;
}
int main()
{
    freopen("/Users/dingning/Desktop/gcj/C-small-attempt1.in","r" ,stdin );
    freopen("/Users/dingning/Desktop/gcj/out.txt","w",stdout);
    
    scanf("%d",&T);
    bool flag;
    bool flag2=1;
    while(T--)
    {
        memset(s,0,sizeof(s));
        scanf("%d%d",&N,&J);
        s[0] = 1;
        s[N-1] = 1;
        for(int i=0;i<=10;i++)
        {
            flag = judge(i);
            if (flag == 0)
                flag2 = 0;
        }
        int ans;
        printf("Case #1: %d",ans);
        
        
        
    }
    return 0;
}
