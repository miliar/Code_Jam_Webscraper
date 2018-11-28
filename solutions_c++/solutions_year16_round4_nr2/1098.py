#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

double ans = 0;
int n, k;
vector<double> p;
    void dfs(int index,int n,int k, vector<int> &comb)
    {
        if (comb.size() == k) {
            vector<vector<double> > yes(k, vector<double>(k + 1, 0));
			yes[0][0] = 1 - p[comb[0]];
			yes[0][1] = p[comb[0]];
			for (int i = 1; i < k; i ++) {
				yes[i][0] = yes[i - 1][0] * (1 - p[comb[i]]);
				for (int j = 1; j <= i + 1; j++) {
					yes[i][j] = yes[i - 1][j] * (1 - p[comb[i]]) + 
						yes[i - 1][j - 1] * p[comb[i]];
				}
			}
			ans = max(ans, yes[k - 1][k / 2]);
        }
        else
        {
            for (int i = index; i < n; i++)
            {
                comb.push_back(i);
                dfs(i + 1,n,k,comb);
                comb.pop_back();
            }
        }
    }


int main() {
	int kase;
	cin >> kase;
	for (int ii = 1; ii <= kase; ii++) {
		cin >> n >> k;
		p.clear();
		p.resize(n);
		for (int i = 0; i < n; i++) {
			cin >> p[i];
		}
		sort(p.begin(), p.end());
		ans = 0;
		vector<int> c;
		dfs(0, n, k, c);
		printf("Case #%d: %.10f\n", ii, ans);
	}
	return 0;
}