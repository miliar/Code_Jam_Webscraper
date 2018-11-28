#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
bool comp(int a,int b)
{return (a>b);}
int main()
{
    int j,t;
    scanf("%d",&t);
    for(j=1;j<=t;j++)
    {
        int mx,i,n,d,a[1000005]={0},rem=0,ans=10000000;
        scanf("%d",&d);
        for(i=0;i<d;i++)
            cin>>a[i];
        sort(a,a+d,comp);
        mx=a[0];
        for(i=1;i<=mx;i++)
        {
            int tm=0,tm1=i;
            for(int k=0;k<d;k++)
            {
                if(a[k]>i)
                {
                    tm+=(a[k]/i);
                    if(a[k]%i==0)
                        tm--;
                }
            }
            tm+=tm1;
            if(tm<ans)
                ans=tm;
        }
        //cout<<re<<endl;
        printf("Case #%d: %d\n",j,ans);
    }
}
