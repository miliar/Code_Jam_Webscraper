#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <map>
#include <string>

#define ForT for(int t=1;t<=T;t++)
#define REP(x,s,n) for(int x=s; x<n; x++)
using namespace std;
typedef long long LL;
typedef long double LD;
//typedef long float LF;

int main() {
    int T;
    freopen("1A.in", "r+", stdin);
    freopen("output.txt", "w+", stdout);
    cin >> T;
    ForT {
        int ans1, ans2, num;
        int sol[17] = {0};
        int ans = 0, count = 0;
        cin >> ans1;
        REP(i,0,4) {
            REP(j,0,4) {
                cin >> num;
                if (i != ans1-1) continue;
		sol[num]++;
            }
        }
        cin >> ans2;
        REP(i,0,4) {
            REP(j,0,4) {
                cin >> num;
                if (i != ans2-1) continue;                                
		sol[num]++;
                if (sol[num] == 2) {
		    ans = num;
                    count++;
                }
            }
        }
	printf("Case #%d: ", t);        	
        if (count == 1) cout << ans << endl;
        else if (count > 1) cout << "Bad magician!" << endl;
        else cout << "Volunteer cheated!" << endl;
    }
    return 0;
}
