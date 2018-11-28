#include <iostream>
#include<cstring>
#include<cstdio>
using namespace std;
long N,T,X;
bool v[12];
bool ok()
{
    for(int i=0; i<=9; i++)
        if(v[i]==false) return false;
    return true;
}

void process(long x)
{
    while(x!=0)
    {
        int tm=x%10;
        v[tm]=true;
        x=x/10;
    }
}

int main()
{
    freopen("w.txt","w",stdout);

    cin>>T;
    for(int TT=1; TT<=T; TT++)
    {
        memset(v,0,sizeof(v));
        cin>>N;
        X=N;
        if(N==0)
        {
            cout<<"Case #"<<TT<<": ";
            cout<<"INSOMNIA"<<endl;
        }
        else
        {
            cout<<"Case #"<<TT<<": ";
            do
            {
                process(X);
                //cout<<X<<" ";
                //for(int i=0;i<=9;i++)cout<<v[i];
                //cout<<endl;
                X=X+N;
            }
            while (!ok());
            cout<<X-N<<endl;
        }
    }
    return 0;
}
