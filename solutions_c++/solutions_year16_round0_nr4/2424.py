#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;
typedef long long LL;

int K,C,S;

void init()
{
     scanf("%d %d %d",&K,&C,&S);
}

void work()
{
     LL x=1,p=0;
     for(int i=1;i<C;i++) x*=K;
     for(int i=1;i<S;i++)
     {
         cout<<p+1<<' ';
         p+=x;
     }
     cout<<p+1<<endl;
}

int main()
{
    int TT;
    scanf("%d",&TT);
    for(int i=1;i<=TT;i++)
    {
        printf("Case #%d: ",i);
        init();
        work();
    }
    return 0;
}

