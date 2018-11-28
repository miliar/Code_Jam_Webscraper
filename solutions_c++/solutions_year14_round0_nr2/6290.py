#include <bits/stdc++.h>
#define ok cout << "ok"
#define open freopen("B-large.in","r",stdin)
#define close freopen("output.txt","w",stdout)
using namespace std;

int main() {
    //open;
    //close;
    int t;
    cin >> t;
    for(int z = 1; z<=t; z++) {
        double C,F,X;
        cin >> C >> F >> X;
        double d = X/2.0;
        double offset = 2.0;
        double farm=0.0;
        while(true) {
            double ffarm = (C/offset);
            farm += ffarm;
            if(farm + (X/(offset+F))<=d) {
                d = farm + (X/(offset+F));
            } else {
                break;
            }
            offset += F;
        }
        cout << "Case #" << z << ": " << fixed << setprecision(7) << d << endl;
    }
    return 0;
}

