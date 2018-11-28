#include <bits/stdc++.h>
using namespace std;
map <char, int> t;
int m [5][5];
map <char, int> cti;
void init (void) {
	cti ['1'] = 0;
	cti ['i'] = 1;
	cti ['j'] = 2;
	cti ['k'] = 3;
	
	m [0 /* 1 */][0 /* 1 */] = 0 /* 1 */;
	m [0 /* i */][1 /* 1 */] = 1 /* i */;
	m [0 /* j */][2 /* 1 */] = 2 /* j */;
	m [0 /* k */][3 /* 1 */] = 3 /* k */;
	
	m [1 /* 1 */][0 /* i */] = 1 /* i */;
	m [1 /* i */][1 /* i */] = 0 /* 1 */ + 4;
	m [1 /* j */][2 /* i */] = 3 /* k */;
	m [1 /* k */][3 /* i */] = 2 /* j */ + 4;
	
	m [2 /* 1 */][0 /* j */] = 2 /* j */;
	m [2 /* i */][1 /* j */] = 3 /* k */ + 4;
	m [2 /* j */][2 /* j */] = 0 /* 1 */ + 4;
	m [2 /* k */][3 /* j */] = 1 /* i */;
	
	m [3 /* 1 */][0 /* k */] = 3 /* k */;
	m [3 /* i */][1 /* k */] = 2 /* j */;
	m [3 /* j */][2 /* k */] = 1 /* i */ + 4;
	m [3 /* k */][3 /* k */] = 0 /* 1 */ + 4;
	
}
int mul (int i, int j) {
	int s = 0;
	if (i >= 4)
	    ++s;
	if (j >= 4)
	    ++s;
	if (m [i % 4][j % 4] >= 4)
	    if (s & 1)
	        return m [i % 4][j % 4] - 4;
	    else
	        return m [i % 4][j % 4];
	else
	    if (s & 1)
	        return m [i % 4][j % 4] + 4;
	    else
	        return m [i % 4][j % 4];
}
int main () {
	ios :: sync_with_stdio (false);
	cin.tie (0);
	freopen ("C:\\C-small-attempt4.in", "r", stdin);
    freopen ("C:\\Users\\bcisag777\\Desktop\\out.txt", "w", stdout);
	init ();
    int t;
    cin >> t;
    for (int c = 1; c <= t; ++c) {
    	int len, rep;
    	string tstr;
    	cin >> len >> rep >> tstr;
    	string str = tstr;
    	while (rep --> 1)
    	    str += tstr;
        int now = 0;
        for (int nres = cti ['1']; nres != cti ['i'] && now < str.length (); ++now)
            nres = mul (nres, cti [str [now]]);
        if (now == str.length ()) {
            cout << "Case #" << c << ": NO" << endl;
            continue;
        }
        for (int nres = cti ['1']; nres != cti ['j'] && now < str.length (); ++now)
            nres = mul (nres, cti [str [now]]);
        if (now == str.length ()) {
            cout << "Case #" << c << ": NO" << endl;
            continue;
        }
        int nres;
        for (    nres = cti ['1']; now < str.length (); ++now)
            nres = mul (nres, cti [str [now]]);
        if (nres != cti ['k']) {
            cout << "Case #" << c << ": NO" << endl;
			continue;
        }  
        cout << "Case #" << c << ": YES" << endl;
    }
	return 0;
}

