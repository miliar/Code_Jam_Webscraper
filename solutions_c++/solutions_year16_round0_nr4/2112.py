#include <math.h>
#include <iostream>


using namespace std;

long long int poww(int base,int ind)
{
    long long int c=1;
    for(int i=0;i<ind;i++)
        c*=base;
    return c;
}

void min(int k, int c)
{
    unsigned long long pos;

    for(int count=c;count<=k;count+=c)
    {
        pos=0;
        for(int t=count-c+1,i=1;t<=count;t++,i++)
        {
            pos+=poww(k,c-i)*(t-1);
        }
        cout<<pos+1<<" ";
        
    }
    if(k%c==0)
        return;
    pos=0;
    for(int t=k-(k%c)+1,i=1;t<=k;t++,i++)
    {
        pos+=poww(k,c-i)*(t-1);
    }
    cout<<pos+1<<" ";
    
}

int main()
{
    int k,c;
    int s,n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>k;
        cin>>c;
        cin>>s;
        if(s<ceil(k*1.0/c))
            cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
        else
        {
            cout<<"Case #"<<i+1<<": ";
            min(k,c);
            cout<<endl;
        }
    }
    
    return 0;
}











