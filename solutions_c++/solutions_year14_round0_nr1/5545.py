#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second

const double pi = acos(-1.0);

int cnt[16];
int tc;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> tc;
    for (int tnum = 0; tnum < tc; tnum++) {
    	for (int i = 0; i < 16; i++)
    		cnt[i] = 0;
    	for (int i = 0; i < 2; i++) {
    		int row;
    		cin >> row;
    		row--;
    		int d;
    		for (int p = 0; p < 4; p++)
    			for (int q = 0; q < 4; q++) {
    				cin >> d;
    				d--;
    				cnt[d] += (row == p);
    			}
    	}
		int ans = 0;
		int any = -1;
		for (int i = 0; i < 16; i++)
			if (cnt[i] == 2) {
				ans++;
				any = i;
			}
		cout << "Case #" << tnum + 1 << ": ";
		if (ans == 0)
			cout << "Volunteer cheated!" << endl;
		else {
			if (ans > 1)
				cout << "Bad magician!" << endl;
		   	else
		   		cout << any + 1 << endl;
		}
    }

    return 0;
}