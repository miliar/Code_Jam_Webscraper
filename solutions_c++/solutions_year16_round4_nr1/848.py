#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <map>

#define sqr(a) (a) * (a)
#define N 200000

using namespace std;


char letter[3] = {'P', 'R', 'S'};
int t[N];
int r, p, s, ttt, tt, i, n;
string ans;
string d[N];

bool ok(int m, int start, int r, int p, int s) {
    int i;
	t[1] = start;
	for (i = 1; i < m; i++) {
		switch(t[i]) {
			case 0:
				t[i * 2] = 1;
				t[i * 2 + 1] = 0;
				break;
			case 1:
				t[i * 2] = 2;
				t[i * 2 + 1] = 1;
				break;
			case 2:
				t[i * 2] = 2;
				t[i * 2 + 1] = 0;
				break;
		}
	}

	for (i = m; i < 2 * m; i++)
		if (t[i] == 0)
			p--;
		else
		if (t[i] == 1)
			r--;
	   	else
	   		s--;

	string temp = "";

	for (i = m; i < 2 * m; i += 2) {
		d[i] = letter[t[i]];
		d[i + 1] = letter[t[i + 1]];
	}

	for (i = m - 1; i >= 1; i--) {
		if (d[i * 2] > d[i * 2 + 1])
			swap(d[i * 2], d[i * 2 + 1]);
		d[i] = d[i * 2] + d[i * 2 + 1];
	}

	if (!s && !p && !r)
		ans = min(ans, d[1]);

	for (i = 1; i < 2 * m; i++)
		d[i] = "";
}

int main()  {

    #ifndef ONLINE_JUDGE
    freopen("a.in", "r" , stdin);
   	freopen("a.out", "w", stdout);
    #endif


    cin >> ttt;

    for (tt = 1; tt <= ttt; tt++) {
    	ans = "z";
    	cin >> n >> r >> p >> s;
   		// 0 - paper
   		// 1 - rock
   		// 2 - scissors
    	for (i = 0; i < 3; i++)
    		ok((1 << n), i, r, p, s);

		if (ans != "z")
			cout << "Case #" << tt << ": " <<  ans << endl;
		else
			cout << "Case #" << tt << ": " << "IMPOSSIBLE" << endl;
    }


    return 0;
}
