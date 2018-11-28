#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <time.h>
using namespace std;
#define LL long long
bool dig[11]= {false};
int digi(int n)
{
    int ans=0;
    while(n>0)
    {
        ans=(n%10);
        n/=10;
        //cout<<"&&"<<n<<" "<<ans<<endl;
        dig[ans]=true;
    }
    //cout<<"&&"<<ans<<endl;
    //dig[ans]=true;
    return ans;
}
bool check()
{
    for(int i=0; i<=9; i++)
        if(dig[i]==false)return false;
    return true;
}
int t,m;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int o=0;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&m);
        if(m==0)
        {
            printf("Case #%d: INSOMNIA\n",++o);
        }
        else
        {
            int ans=0;
            for(int i=0; i<=9; i++)dig[i]=false;
            digi(m);
            while(!check())
            {
                digi(m*(ans+2));
                ans++;
            }
            printf("Case #%d: %d\n",++o,m*(ans+1));
        }


    }
}








