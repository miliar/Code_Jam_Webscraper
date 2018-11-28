#include<iostream>
#include<cstdio>
#include<cstring>
#define LL long long
using namespace std;

int main()
{
    #ifndef ONLINE_JUDGE
        freopen("input.cpp","r",stdin);
        freopen("output.cpp","w",stdout);
    #endif // ONLINE_JUDGE
    char s[10005];
    int t,i,smax,res,till_here,test;
    scanf("%d",&test);
    t=1;
    while(t<=test)
    {
        printf("Case #%d: ",t);
        t++;
        scanf("%d",&smax);
        scanf("%s",s);
        res=0;
        till_here=s[0]-48;
        for(i=1;i<=smax;i++)
        {
            if(till_here>=i)
            {
                till_here+=(s[i]-48);
            }
            else
            {
                res=res+(i-till_here);
                till_here+=(i-till_here);
                till_here+=(s[i]-48);
            }
        }
        printf("%d\n",res);
    }
    return 0;
}
