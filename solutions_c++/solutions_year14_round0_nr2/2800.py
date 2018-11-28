#include <iostream>
#include <stdio.h>
#include <vector>
#include <limits>
#include <iomanip>
using namespace std;

int main() {
    int cnt;
    freopen("B-large.in", "r", stdin);
    freopen("b-large.out", "w", stdout);
    cin >>cnt;
    for(int t=1; t<=cnt; ++t) {
        double c,f,x;
        cin>>c>>f>>x;
        int farmNum = (x*f-2*c)/(c*f);
        double time = 0;
        if(farmNum<=0) {
            time = x/2.0;
        } else {
            for(int i=1; i<=farmNum; ++i) {
                time += c/(2+(i-1)*f);
            }
            time += x/(2+farmNum*f);
        }
        cout<<"Case #"<<t<<": "<<setiosflags(ios::fixed)<<setprecision(7)<<time<<endl;
    }
    return 0;
}
