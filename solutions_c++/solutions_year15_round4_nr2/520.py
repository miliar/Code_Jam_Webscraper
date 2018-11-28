#include <iostream>
#include <vector>
#include <cstdio>
#include <set>
#include <map>
#include <fstream>
#include <algorithm>
#include <map>
#include <queue>


using namespace std;

int t;
long double r[300];
long double x[300];
long double v, ho;
int n;
int main()
{
    cout.precision(10);
    cout << fixed;
    freopen("B-small-attempt2.in", "r", stdin);
    freopen("B.out", "w", stdout);
    cin >> t;

    for (int ttt=1;ttt<=t;ttt++) {
        cout << "Case #" << ttt<<": ";
        cin >> n;
        cin >> v>>ho;
        if (n==1) {
            cin >> r[1]>>x[1];
            if (x[1]!=ho) {
                cout << "IMPOSSIBLE"<<endl;
            }
            else {
                long double sol=v/r[1];
                cout << sol<<endl;
            }
        }
        if (n==2) {
            cin >> r[1]>>x[1];
            cin >> r[2]>>x[2];
            if (x[1]==x[2]) {
                if (x[1]!=ho) cout << "IMPOSSIBLE"<<endl;
                else {
                    long double sol=v/(r[1]+r[2]);
                    cout << sol<<endl;
                }
            }
            else {
                long double egyik=(ho-x[2])/(x[1]-x[2]);
                egyik*=v;
                long double masik=v-egyik;
                if (egyik<0 || masik<0) cout << "IMPOSSIBLE"<<endl;
                else {
                    long double sol=max(egyik/r[1], masik/r[2]);
                    cout << sol<<endl;
                }
            }
        }
    }


    return 0;
}
