#define debug if(0)
// Grzegorz Guspiel
#include <bits/stdc++.h>
using namespace std;
 
#define REP(i,n) for(int i=0;i<int(n);++i)
#define SIZE(c) ((int)((c).size()))
#define FOREACH(i,x) for (__typeof((x).begin()) i=(x).begin(); i!=(x).end(); ++i)
#define ALL(v) (v).begin(), (v).end()
#define pb push_back
#define mp make_pair
#define st first
#define nd second

template<typename T> void maxE(T& a, const T& b) { a = max(a, b); }
template<typename T> void minE(T& a, const T& b) { a = min(a, b); }

const double EPS = 1e-9;

int main() {
    ios_base::sync_with_stdio(0);
	int z; cin >> z;
    for (int zz = 1; zz <= z; zz++) {
        double cost, farmBonus, cookieGoal;
        cin >> cost >> farmBonus >> cookieGoal;
        double t = 0;
        double cookies = 0;
        double speed = 2;
        while (cookies < cookieGoal - EPS) {
            debug cout << "cookies " << cookies << " speed " << speed << " cost " << cost <<  endl;
            double noFarm = (cookieGoal - cookies) / speed;
            double withFarm = (cookieGoal - cookies + cost) / (speed +farmBonus);
            if (cookies < cost - EPS) {
                withFarm = INFINITY;
            }
            if (withFarm < noFarm) {
                speed += farmBonus;
                cookies -= cost;
            } else {
                double passes = (cookieGoal - cookies) / speed;
                if (cookies < cost - EPS) {
                    passes = min(passes, (cost - cookies) / speed);
                }
                debug cout << "pass " << passes << endl;
                t += passes;
                cookies += passes * speed;
            }
        }
        cout.precision(8);
        cout << "Case #" << zz << ": " << fixed << t << endl;
	}
	return 0;
}
