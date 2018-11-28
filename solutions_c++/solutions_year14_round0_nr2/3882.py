#include <iostream>
#include <iomanip>
#include <cstdio>

using namespace std;

int main(){
    freopen ("bsmall.out","w",stdout);
    int t;
    cin>>t;
    for (int tc=1;tc<=t;tc++){
        long double c,f,x;
        cin>>c>>f>>x;
        long double ma=1e10;
        long double bt=0;
        long double p=2;
        while (bt<ma) {
            ma=min(ma,bt+x/p);
            bt+=c/p;
            p+=f;
        }
        cout <<"Case #"<<tc<<": ";
        cout <<setprecision(10)<<ma<<endl;
    }
}
