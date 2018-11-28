#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;

typedef vector<int>vi;
typedef pair<int,int>ii;
typedef vector<ii>vii;
#define M 1000000007
const int INF = (int) 1e9;
const int MAX = (int) 1e5 + 10;
map<ll,int>ma ;
bool fun(ll temp)
{
    bool flag=true ;
     while(temp!=0)
        {
            int k = temp%10 ;
            if(ma.find(k) == ma.end())
               ma[k]=1;
            else
                ma[k]++;
            temp/=10;
        }
        for(int i=0;i<10;i++)
        {
            if(ma[i]==0)
                flag=false ;
        }
        return flag ;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("outpu.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int co=1,n;
    while(t--)
    {
    ma.clear();
        printf("Case #%d: ",co++);
        scanf("%d",&n);
        if(n==0)
            {
                printf("INSOMNIA\n");
                continue ;
            }


        ll temp =n ,la=2;
        fun(temp);
        while(1)
        {
            temp = n*la;
           bool flag = fun(temp);
           if(flag or la>200 )
            break ;
            la++;
        }
        printf("%lld\n",temp);
    }
    return 0;
}
