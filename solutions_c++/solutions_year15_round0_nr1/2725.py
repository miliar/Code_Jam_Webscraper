#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <bitset>
#include <numeric>
#include <ctime>
#include <cassert>
#include <algorithm>

using namespace std;

typedef pair<int, int> PII;
typedef long long ll;

#define fi first
#define se second
#define mp make_pair
#define pb push_back

int main() {
	int _; cin >> _; 
	for (int __ = 1; __ <= _; __ ++) {
        printf ("Case #%d: ", __);
        int N;
        string str;
        cin >> N >> str;
        if (N == 0) {
           printf ("0\n");
        } else {
           vector<int> aud;
           for (int i = 0; i < str.size(); ++i) {
               aud.push_back(str[i] - '0');
           }
           int sum = 0;
           int need = 0;
           for (int i = 0; i < N + 1; ++i) {
               if (sum >= i) {
                  sum += aud[i];
               } else if (aud[i] == 0) {
                  continue;
               } else {
                  need += i - sum;
                  sum = i + aud[i];
               }
           }
           printf ("%d\n", need);
        }
	}
	return 0; 
}
