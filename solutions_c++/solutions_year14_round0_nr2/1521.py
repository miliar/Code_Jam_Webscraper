#include<cstdio>
#include<fstream>
#include<iostream>
#include<algorithm>
using namespace std;
int t;
double best,cost,inc,tar,tim;
int main()
{
    freopen("blarge.in","r",stdin);
    freopen("blarge.out","w",stdout);
    cin>>t;
    for(int test=1;test<=t;test++)
    {
        cin>>cost>>inc>>tar;
        best=tar/2;
        tim=0;
        for(int i=1;i<=100000;i++)
        {
            tim+=cost/(2+inc*(i-1));
            best=min(best,tim+tar/(2+inc*i));
        }
        printf("Case #%d: %.7f\n",test,best);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
