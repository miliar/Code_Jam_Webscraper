#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cstdlib>
#include <stack>
using namespace std;

int txt(long double a) 
{
    int l=0;
    
    while(a>=1)
    {
        l++;
        a/=10;
    }
    
    return l;
}

int main () 
{
    int zestaw;
    cin>>zestaw;
    
    for(int i = 0; i < zestaw; i++)
    {
        long double cwel, f, x;
        cin>>cwel>>f>>x;
        cout<<"Case #"<<i+1<<": ";
        long double p, t;
        t=0;
        p=2;

        long double T=x/p;
        long double M=T;
        while(t<=T && t<=M) {
            M=min(t+x/p, M);
            t+=cwel/p;
            p+=f;
        }

        int l=txt(M);
        cout.precision(7+l);
        cout<<M<<endl;
    }
    return 0;
}
