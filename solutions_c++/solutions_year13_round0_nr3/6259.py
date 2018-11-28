#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
#define LL long long
int judge(LL x)
{
    int y[110],wei=0;
    while(x)
    {
        y[wei]=x%10;
        x/=10;
        wei++;
    }
    int bo=1;
    for(int i=0;i<wei;i++)
    if(y[i]!=y[wei-1-i])
    bo=0;
    return bo;
}
int main()
{
    int T;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("test.out","w",stdout);
    cin>>T;
    for(int cas=1;cas<=T;cas++)
    {
        LL a,b;
        cin>>a>>b;
        a--;
        LL l=0,r=0,i=1;
        while(i*i<=b)
        {
            if(judge(i)&&judge(i*i))
            {
                if(i*i<=a)
                l++;
                if(i*i<=b)
                r++;
            }
            i++;
        }
        printf("Case #%d: ",cas);
        cout<<r-l<<endl;
    }
    return 0;
}
