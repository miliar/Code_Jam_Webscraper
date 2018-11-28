#include <iostream>
#include <fstream>

using namespace std;

long long T,N,n,t;
int sz;
bool v[10];

int main()
{
    freopen("A-large.in.txt","r",stdin);
    freopen("A-large.out.txt","w",stdout);
    cin>>T;
    for(int k=1;k<=T;k++)
    {
        cin>>N;
        cout<<"Case #"<<k<<": ";
        if(N==0)
        {
            cout<<"INSOMNIA"<<endl;
            continue;
        }
        for(int i=0;i<10;++i)
            v[i]=false;
        sz=10;
        n=0;
        while(sz>0)
        {
            n+=N;
            t=n;
            while(t>0)
            {
                if(!v[t%10])
                {
                    v[t%10]=true;
                    --sz;
                }
                t/=10;
            }
        }
        cout<<n<<endl;
    }
}
