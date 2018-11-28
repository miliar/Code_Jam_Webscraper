#include<iostream>
#define fri(n) for(int i=0;i<n;i++)
#define frj(n) for(int j=0;j<n;j++)
using namespace std;
int main() {
	freopen("A-small-attempt1.in","r",stdin);
	freopen("output.in","w",stdout);
	int t;
	cin >> t;
	for (int caseno = 1; caseno <= t; caseno++) {
		int n, m, ans = 0, finans = 0;
		cin >> n;
		n--;
		int a[4][4], b[4][4];
		fri(4)
			frj(4)
				cin >> a[i][j];
		cin >> m;
		m--;
		fri(4)
			frj(4)
				cin >> b[i][j];
		fri(4)
		{
			frj(4)
			{
				if (a[n][i] == b[m][j]) {
					if (ans != 0) {
						finans = 2;
						break;
					} else
					{
						ans=a[n][i];
						finans = 1;
					}
				}
			}
		}
		cout << "Case #" << caseno << ": ";
		if (finans == 2)
			cout << "Bad magician!\n";
		else if (finans)
			cout << ans << "\n";
		else
			cout << "Volunteer cheated!\n";

	}
	return 0;
}
