#include"bits/stdc++.h"
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef long long int lli;
typedef long double ld;
typedef pair<long long int,long long int> pll;
typedef vector<int> vi;
const ld EPS = 1e-12;
#define rep(i,a,b) for(int i=a;i<b;i++)
#define rof(i,a,b) for(int i=a;i>b;i--)
#define pb push_back
#define mp make_pair
#define inf 1000000000
#define mod 1000000007
#define mst(a,b) memset(a,b,sizeof(a))
#define pi (double)(3.141592653589793)

long long int n,t;
long long int sum;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    int i;

    for(i=1;i<=t;i++)
    {
       cin>>n;
       sum=n;
       if(n==0)
       {
           cout<<"Case #"<<i<<": INSOMNIA"<<endl;
           continue;
       }
       long long int cnt=1;
       long long int a[10];
       memset(a,0,sizeof(a));
       while(cnt<= 1000000)
       {
            sum=n*cnt;
            while(sum>0)
           {
                int temp=sum%10;
                a[temp]=1;
                sum/=10;
           }

           int total=0;
           for(int j=0;j<10;j++)
           {
               if(a[j]==1)
                total++;
               else
                break;
           }
           if(total==10)
            {
                cout<<"Case #"<<i<<": "<<n*cnt<<endl;
                break;
            }


           cnt++;
       }
       if(cnt> 1000000)
       cout<<"Case #"<<i<<": INSOMNIA"<<endl;

    }



   return 0;

}
