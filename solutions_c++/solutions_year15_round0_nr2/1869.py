#include <bits/stdc++.h>

using namespace std;

const int NMAX = 1e3+5;
const int INF = (1<<30);

ifstream f("test.in");


int pi[NMAX];

void scrie(int noTest, int ans){
    printf("Case #%d: %d\n", noTest, ans);
}


int main(){
    freopen("test.out", "w", stdout);
int t;
    f >> t; for(int noTest=1; noTest<=t; ++noTest){
        int d; f >> d;
        int maxPi = 0;
        for(int i=1; i<=d; ++i){
            f >> pi[i];
            maxPi = max(maxPi, pi[i]);
        }

        int ans = INF;
        for(int ansFixed = 1; ansFixed <= maxPi; ++ansFixed){
            int specialMinutes = 0;
            for(int i=1; i<=d; ++i){
                if (pi[i] > ansFixed){
                    specialMinutes += pi[i] / ansFixed;
                    if (pi[i]%ansFixed == 0) --specialMinutes;
                }
            }
            ans = min(ans, ansFixed + specialMinutes);
        }


        scrie(noTest, ans);
    }

    return 0;
}
