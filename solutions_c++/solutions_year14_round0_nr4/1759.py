#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
double TJ[10008],King[10008],TJ1[10008];
bool cmp(double a,double b)
{
    return a>b;
}
int n,m;
void solve()
{
    for(int i=n-1;i>=1;i--)
    {
            TJ[i] = TJ[i-1] ;
    }
}
void solve1()
{
   for(int i=n-1;i>=1;i--)
    {
            King[i] = King[i-1] ;
    }
}
int main()
{
    int T;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    int cn = 0;
    while(T--)
    {
        cin >> n;
        for(int i=0;i<n;i++){cin>>TJ[i]; }
        for(int i=0;i<n;i++)cin>>King[i];
        sort(King,King+n,cmp);
        sort(TJ,TJ+n,cmp);
         for(int i=0;i<n;i++){TJ1[i] = TJ[i]; }
        int sum = 0,sum1 = 0;
        for(int i=0;i<n;i++)
        {
            if(King[i] < TJ[i])sum++;
            else
               solve();
        }
        for(int i=0;i<n;i++)
        {
            if(King[i]  > TJ1[i])sum1++;
            else
               solve1();
        }
       printf("Case #%d: %d %d\n",++cn,sum,n-sum1);

    }
}
