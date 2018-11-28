#include <bits/stdc++.h>

using namespace std;

void resolver(int n, int t, int j)
{
    int i, v = 0, a;
    if(n!=0)
    {
        for(i=n;v!=1023;i+=n)
        {
            a = i;
            while(a!=0)
            {
                v = (v|(1<<(a%10)));
                a/=10;
            }
        }
        cout<<"Case #"<<j<<": "<<i-n<<endl;
    }
    else
    {
        cout<<"Case #"<<j<<": INSOMNIA"<<endl;
    }
}

int main()
{
    /*int i;
    for(i=1;i<1000000;i++)
    {
        resolver(i, 0, 0);
    }*/
    int t, j, n;
    cin>>t;
    for(j=1;j<=t;j++)
    {
        cin>>n;
        resolver(n, t, j);
    }
    return 0;
}
