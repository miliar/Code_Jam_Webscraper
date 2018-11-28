#include<iostream>

using namespace std;

int main()
{
    long T,n,m,o,c,a;
    cin>>T;
    long *p=new long[T];
    for(int t=1;t<=T;t++)
    {
        cin>>n>>m>>o;
        cin>>a;
        if(a<o){
            p[t]=-1;
            for(int i=1;i<n;i++)cin>>a;
            continue;
        }
        c=1;
        for(int i=1;i<n;i++)
        {
            cin>>a;
            if(a>=o)c++;
        }
        p[t]=c;
    }
    for(int t=1;t<=T;t++)
    {
        cout<<p[t]<<endl;
    }
}
