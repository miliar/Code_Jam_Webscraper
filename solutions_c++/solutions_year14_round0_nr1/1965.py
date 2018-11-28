#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cstdlib>

typedef long long int lli;
typedef long int li;

#define F(i, n) for(i = 0;i < n; ++i)
#define FI(i, st, ft) for(i = st;i <= ft; ++i)
#define pb(a, b) a.push_back(b)

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int a, i, j, k, t;
	cin >> t;
	F(k, t){
		int a[5][5], b[5][5], ans1, ans2;
		vector <int> ans;
		cin >> ans1;
		--ans1;
		F(i, 4){
			F(j, 4){
				cin >> a[i][j];
			}
		}
		cin >> ans2;
		--ans2;
		F(i, 4){
			F(j, 4){
				cin >> b[i][j];
			}
		}
		F(i, 4){
			F(j, 4){
				if(a[ans1][i] == b[ans2][j]){
					pb(ans, a[ans1][i]);
				}
			}
		}	
		cout << "Case #" << k + 1<< ": ";
		if(ans.size() == 1) cout << ans[0] << "\n";
		else if(ans.size() == 0) cout << "Volunteer cheated!" << "\n";
		else cout << "Bad magician!" << "\n";
	}
	return 0;
}
