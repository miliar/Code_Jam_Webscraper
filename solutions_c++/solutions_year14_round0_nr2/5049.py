#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

int main() {
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    double c,f,x,res;
    cin >> t;
    for(int i=1;i<=t;i++) {
        res = 0.0;
        double avg = 2.0;
        double tot = 0.0;
        cin >> c >> f >> x;
        while(true) {
            if(tot >= x) break;
            if(tot >= c) {
                double t1 = (x + c - tot) / (avg + f);
                double t2 = (x - tot) / avg;
                if(t1 >= t2) {
                    res += t2;
                    tot = x;
                }
                else {
                    tot -= c;
                    res += c / avg;
                    avg += f;
                }
            }
            else {
                double t1 = (c - tot) / avg + x / (avg + f);
                double t2 = (x - tot) / avg;
                if(t1 >= t2) {
                    res += t2;
                    tot = x;
                }
                else {
                    res += (c - tot) / avg;
                    tot = 0;
                    avg += f;
                }
            }
        }
        cout << "Case #" << i << ": ";
        printf("%.7f\n",res);
    }
    return 0;
}
