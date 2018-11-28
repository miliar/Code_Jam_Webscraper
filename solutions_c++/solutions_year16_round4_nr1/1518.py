#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <cstring>
#include <cmath>
using namespace std;
#define MAXN 1000000
typedef long long int ll;
typedef pair<int,int> pii;

int n, nn;

char getMax(char x, char y) {
    char c[3] = {x, y, 0};
    sort(c, c + 2);
    if (strcmp(c, "PR") == 0) {
        return 'P';
    }
    if (strcmp(c, "PS") == 0) {
        return 'S';
    }
    if (strcmp(c, "RS") == 0) {
        return 'R';
    }
    return 0;
}

bool isvalid(char* s) {
    string t = s;
    while (t.size() > 1) {
        string q;
        
        for (int i = 0; i < (int)t.size(); i += 2) {
            char c = getMax(t[i], t[i + 1]);
            if (!c) {
                return false;
            }
            q += c;
        }
        
        t = q;
    }
    
    return true;
}

int main() {
	ios_base::sync_with_stdio(0);
	
	freopen("A.test.in", "r", stdin);
	//freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small.out", "w", stdout);

	int testcases;
	cin >> testcases;

	for (int testcase = 1; testcase <= testcases; testcase++) {
		cout << "Case #" << testcase << ": ";
		
		int r, p, s;
		cin >> n >> r >> p >> s;
		nn = 1 << n;
		
		// given: RPS
		// todo:  PRS
		static char arr[(1 << 12) + 1];
		memset(arr, 0, sizeof arr);
		
		for (int i = 0; i < nn; i++) {
            if (i < p) {
                arr[i] = 'P';
            } else if (i < p + r) {
                arr[i] = 'R';
            } else {
                arr[i] = 'S';
            }
		}
		arr[nn] = 0;
		
		string res;
		
		do {
                //cout << arr << endl;
            if (isvalid(arr)) {
                res = arr;
                break;
            }
		}while (next_permutation(arr, arr + nn));
		
		if (res.size() == 0) {
            res = "IMPOSSIBLE";
		}
		
		cout << res << endl;
	}

	return 0;
}

