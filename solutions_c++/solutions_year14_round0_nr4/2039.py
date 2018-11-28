// 1A_A.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main(int argc, char* argv[])
{
    freopen ("D-large.in", "r", stdin);
    freopen ("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int k = 0; k < T; ++k) {
        deque <double> naomi_war, ken_war;
        int n;
        cin >> n;
        for (int i = 0; i < n; ++i) {
            double a;
            cin >> a;
            naomi_war.push_back (a);
        }
        for (int i = 0; i < n; ++i) {
            double a;
            cin >> a;
            ken_war.push_back (a);
        }
        sort (naomi_war.begin (), naomi_war.end ());
        sort (ken_war.begin (), ken_war.end ());
        int points = n, dpoints = 0;
        deque <double> naomi_dwar (naomi_war), ken_dwar (ken_war);
        for (int i = 0; i < n; ++i) {
            if ((naomi_dwar.front () > ken_dwar.front ()) && (ken_dwar.back () != 1.0)) {
                dpoints++;
                naomi_dwar.pop_front ();
                ken_dwar.pop_front ();
            }
            else {
                naomi_dwar.pop_front ();
                ken_dwar.pop_back ();
            }
        }
        int naomi_pos = 0;
        for (int i = 0; i < n; ++i) {
            if (naomi_war [naomi_pos] < ken_war [i]) {
                --points;
                ++naomi_pos;
            }
        }
        cout << "Case #" << k + 1 << ": " << dpoints << " " << points << endl;
    }
	return 0;
}

