/**
*
*/
#include <bits/stdc++.h>
#define MAXN 100002
#define INF 200000000

typedef long long ll;
using namespace std;
string s;
int as[MAXN + 2], bs[MAXN + 2];

int n, k;
double pi[20];

double max_res = 0.0, resd = 0.0;

void subset2(vector <double> &A, int k, int start, int currLen, bool used[]) {

		if (currLen == k) {
            double first = 1.0;
			for (int i = 0; i < A.size(); i++) {
				if (used[i] == true) {
                    first *= A[i];
				}
				else first *= (1 - A[i]);

			}

			resd += first;
			return;
		}
		if (start == A.size()) {
			return;
		}
		used[start] = true;
		subset2(A, k, start + 1, currLen + 1, used);

		used[start] = false;
		subset2(A, k, start + 1, currLen, used);
	}

void subset(int k, int start, int currLen, bool used[]) {

		if (currLen == k) {
            vector <double> ps;
            resd = 0.0;
			for (int i = 0; i < n; i++) {
				if (used[i] == true) {
				    ps.push_back(pi[i]);
				}
			}
			bool used2[20]; for(int i = 0; i < 20; ++i) used2[i] = false;
            subset2(ps, k / 2, 0, 0, used2);
            //cout << "**" << resd << endl;
            max_res = max(max_res, resd);
			return;
		}
		if (start == n) {
			return;
		}
		used[start] = true;
		subset(k, start + 1, currLen + 1, used);

		used[start] = false;
		subset(k, start + 1, currLen, used);
	}

int main() {
    freopen("B-small-attempt1 (2).in", "r", stdin);
    freopen("ancestor.out", "w", stdout);

    int t; cin >> t; for(int i = 0; i < t; ++i) {
        max_res = 0.0;
        cin >> n >> k;
        for(int i = 0; i < n; ++i) cin >> pi[i];
        bool used[20]; for(int i = 0; i < 20; ++i) used[i] = false;
        subset(k, 0, 0, used);
        cout << fixed << setprecision(7) << "Case #" << i + 1 << ": " << max_res << endl;
    }

}
