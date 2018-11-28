#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        long long n;
        long long res;
        cin>>n;
        int k[11]={0};
        int cont = 0;
        long long a=1;
        for(a=1;a<=10000;a++)
        {
            res = n * a;
            while ( res > 0)
            {
                long long aux = res % 10;
                if(k[aux]==0)
                {
                    cont++;
                    k[aux]=1;
                }
                res = res / 10 ;
            }
            if(cont == 10 )
            {
                res = n * a;
                break;
            }
        }
        if(cont==10)
            cout<<"Case #"<<i<<": "<<res<<endl;
        else
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
    }
    return 0;
}
