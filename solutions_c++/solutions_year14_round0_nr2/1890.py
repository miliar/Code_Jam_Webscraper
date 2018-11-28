#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

double c,f,x;

int main() {
    int TT;
    cin>>TT;
    for(int T=1;T<=TT;T++) {
        cin>>c>>f>>x;
        double s=2.0;
        double ans=x/s,t=0;
        while(1) {
            t+=c/s;
            s+=f;
            double a=t+x/s;
            if (a<ans) ans=a;
            else break;
        }
        cout<<"Case #"<<T<<": ";
        cout<<setprecision(20)<<ans;
        cout<<endl;
    }
    return 0;
}