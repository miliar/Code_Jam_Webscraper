#include <bits/stdc++.h>
using namespace std;
char s[1000];
#define pb push_back
#define mp make_pair
#define ll long long int
vector<char>V;
int d[20];
int main()
{
    ll t,i,count,ans;
    freopen("1.in","r",stdin);
   freopen("2.out","w",stdout);
    char prev;
  cin>>t;
  int temp;
    ll j=1;
   ll a,a1;
    while(t>0)
    {
        t--;
        cin>>a;
        memset(d,0,sizeof(d));
        if(a==0)
        {
            cout<<"Case #"<<j<<": INSOMNIA"<<endl;
        }
        else
        {
            a1=a;
            while(true)
            {
                temp=a;
                while(temp>0)
                {
                    d[temp%10]++;
                    temp=temp/10;
                }
                for(i=0;i<10;i++)
                {
                    if(d[i]==0)
                        break;
                }
                if(i==10)
                {
                    break;
                }
                a=a+a1;
            }
            cout<<"Case #"<<j<<": "<<a<<endl;
        }
        j++;
    }
}
