#include <iostream>
#include <cstdio>

using namespace std;

long D[20],casos,caso,m,n,u,a,x;

void digitos(long n,long in)
{
    if (in<=n)
    {
        x=(n%(in*10))/in;
        if (D[x]==0)
        {
            u++;
            D[x]=1;
        }
        digitos(n,in*10);
    }
}

int main()
{
    freopen("i2.in","r",stdin);
    freopen("o2.out","w",stdout);
    cin>>casos;
    caso=1;
    while (casos--)
    {
        cin>>n;
        cout<<"Case #"<<caso++<<": ";
        m=n;
        u=0;
        if (n!=0)
        {
            for (a=0;a<=9;a++) D[a]=0;
            while (u!=10)
            {
                digitos(n,1);
                n+=m;
            }
            cout<<n-m<<endl;
        }
        else cout<<"INSOMNIA"<<endl;
    }
    fclose(stdin);
    fclose(stdout);
}
