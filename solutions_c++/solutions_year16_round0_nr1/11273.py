#include<iostream>
#include<cstring>
#define ll long long int
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    int t,k;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        bool f=false;
        int n,m;
        cin>>n;
        m=0;
        int v[10]={0};
        if(n==0)
            cout<<"Case #1: INSOMNIA\n";
        else
        {
        while(1)
        {
            f=true;
            m+=n;
            int x=m;
            while(x)
            {
                v[x%10]=1;
                x/=10;
            }
            for(int i=0;i<10;i++)
            {
                if(!v[i])
                    f=false;
            }
            if(f==true)
                break;
        }
        cout<<"Case #"<<k<<": "<<m<<endl;
        }
    }
    return 0;
}
