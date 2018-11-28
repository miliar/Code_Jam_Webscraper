#include<iostream>
#include<cstdio>
#define gc getchar_unlocked
void scanint(int &x)
{
    register int c = gc();
    x = 0;
    for(;(c<48 || c>57);c = gc());
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
}
using namespace std;
int main()
{
    int t,p,q,f=1,count=0,t1=1;
    cin>>t;
    while(t--)
    {
        f=1;
        count=0;
        scanint(p);
        scanint(q);
        if(q%2!=0)
            f=0;
        if(f)
        {
            while(p<q)
            {
                count++;
                q=q/2;
            }
        }
        cout<<"Case #"<<t1++<<": "<<count<<endl;
    }
    return 0;
}
