#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

using namespace std;

const int MAXN = 222;
const int MAXM = 5555;
const int MAXBUF = 100100;

int n, m;
map<string, int> word_to_int;
char buffer[MAXBUF];
vector<int> words[MAXN];
int a[MAXN];
int b[MAXM];

void solve() {
    m = 0;
    word_to_int.clear();

    scanf("%d\n", &n);
    for (int i = 0; i < n; i++) {
        words[i].clear();

        gets(buffer);
        int len = strlen(buffer);
        buffer[len] = ' ';
        string current = "";
        for (int j = 0; j <= len; j++) {
            if (buffer[j] == ' ') {
                if (current != "") {
                    if (word_to_int[current] == 0) {
                        word_to_int[current] = ++m;
                    }
                    words[i].push_back(word_to_int[current] );
                    // cerr << current << " " << word_to_int[current] << "\n";
                }
                current = ""; 
                continue;
            } 
            current += buffer[j];
        }
    }

    int answer = m;
    for (int mask = 0; mask < (1 << n); mask++) {
        for (int i = 0; i < n; i++) {
            a[i] = (mask & (1 << i) ) > 0;
        }
        if (a[0] == a[1] ) {
            continue;
        }

        for (int i = 1; i <= m; i++) {
            b[i] = 0;
        }

        for (int i = 0; i < n; i++) {
            for (int c : words[i] ) {
                b[c] |= 1 << a[i];
            }
        }

        int count = 0;
        for (int i = 1; i <= m; i++) {
            if (b[i] == 3) {
                count += 1;
            }
        }

        answer = min(answer, count);
    }

    cout << answer << "\n";
}

int main() {
	int cases; cin >> cases;
	for (int i = 0; i < cases; i++) {
        cout << "Case #" << i + 1 << ": ";
        solve();
        cerr << i + 1 << " is done!\n";
    }
    return 0;
}