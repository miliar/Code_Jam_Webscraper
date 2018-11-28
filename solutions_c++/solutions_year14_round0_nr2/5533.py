#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int t;
    cin>>t;
    for(int i = 0; i < t; ++i) {
        cout<<"Case #"<<i+1<<": ";
        double c,f,x;
        cin>>c>>f>>x;
        double best = x/2;
        double rate = 2;
        double time = 0;
        for(int i = 0; i < 3e5; ++i) {
            time += c/rate;
            rate += f;
            best = min(best, time + x/rate);
        }
        cout<<fixed;
        cout<<setprecision(10)<<best<<'\n';

    }
}
