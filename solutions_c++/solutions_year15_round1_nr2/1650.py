#include <iostream>
#include <cstdio>
using namespace std;
long long gcd(long long a,long long b)
{
    return b==0?a:gcd(b,a%b);
}
long long barber[1005];
int main()
{
    freopen("B-small-attempt3.in","r",stdin);
    freopen("B-small-attempt3.out","w",stdout);
    int T=0,caseT=1;
    cin>>T;
    while (T--)
    {
        int m,N;
        cin>>m>>N;
        for (int i=0;i<m;i++)
        {
            cin>>barber[i];
        }
        long long a=barber[0],b=barber[1];
        for (int i=1;i<m;i++)
        {
            b=barber[i];
            a=a*b/gcd(a,b);
        }
        int p=0;
        for (int i=0;i<m;i++)
        {
            p+=a/barber[i];
        }
        int res=N%p+p;
        int t[1005],cnt=0;
        for (int i=0;i<m;i++)
        {
            t[i]=0;
        }
        int flag=0;
        for (int j=0;j<10000000;j++)
        {
            if (flag==1) break;
                
            for (int i=0;i<m;i++)
            {
                if (t[i]==0)
                {
                    t[i]=barber[i];
                    t[i]--;
                    cnt++;
                }
                else
                    t[i]--;
                if (cnt==res)
                {
                    cout<<"Case #"<<caseT++<<": "<<i+1<<endl;
                    flag=1;
                    break;
                } 
            }
        }

    }
    return 0;
}
