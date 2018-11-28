#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>t
#include<cstdlib>
using namespace std;

int txt(long double a) {
    int l=0;
    while(a>=1)
    {
        l++;
        a/=10;
    }
    return l;
}

int main () {
    int Z;
    cin>>Z;
    for(int tt=0; tt<Z; tt++)
    {
        long double c, f, x;
        cin>>c>>f>>x;
        cout<<"Case #"<<tt+1<<": ";
        long double p, t;
        t=0;
        p=2;

        long double T=x/p;
        long double M=T;
        while(t<=T && t<=M) {
            M=min(t+x/p, M);
            t+=c/p;
            p+=f;
        }

        int l=txt(M);
        cout.precision(7+l);
        cout<<M<<endl;
    }
    return 0;
}
