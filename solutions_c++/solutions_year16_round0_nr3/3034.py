#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#define MAXN 32

using namespace std;

int T,N,J,v[MAXN];

int f(int i)
{
    if(i==N-1)
    {
        int p=0,d=0;
        for(i=0;i<N;i++)
            if(v[i])
            {
                if(i%2)
                    d++;
                else
                    p++;
            }
        if(d==p)
        {
            for(i=0;i<N;i++)
                cout<<v[i];
            cout<<" 3 4 5 6 7 8 9 10 11"<<endl;
            if(--J==0)
                exit(0);
        }
    }
    else
    {
        v[i]=0;
        f(i+1);
        v[i]=1;
        f(i+1);
    }
}

int main()
{
    //freopen("A-large.in.txt","r",stdin);
    freopen("A-large.out.txt","w",stdout);
    cin>>T;
    for(int k=1;k<=T;k++)
    {
        cin>>N>>J;
        cout<<"Case #"<<k<<":"<<endl;
        for(int i=0;i<N;i++)
            v[i]=0;
        v[0]=1;
        v[N-1]=1;
        f(1);
    }
}
