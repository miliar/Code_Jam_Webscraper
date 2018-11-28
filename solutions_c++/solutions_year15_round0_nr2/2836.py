#include <iostream>
#include <set>
#include <map>
#include <cmath>

using namespace std;

int main()
{
    int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
        int D, P[1000];
        cin >> D;
        int highest = 0;
        for (int i = 0; i < D; i++) {
            cin >> P[i];
            if (P[i] > highest)
                highest = P[i];
        }
        int best = highest;
        while (highest --> 1) {
            int specials = highest;
            for (int i = 0; i < D; i++) {
                specials += P[i] / highest - (P[i] % highest == 0);
            }
            if (specials < best)
                best = specials;
        }
        cout << "Case #" << t << ": " << best << "\n";
        
	}
	return 0;
}
