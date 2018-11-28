#include<iostream>
#include<iomanip>
#define li long int
#define ulli long long int
#define fri(n) for(li i=0;i<n;i++)
#define frj(n) for(li j=0;j<n;j++)
using namespace std;
bool traverse(int ** a, int k, int l, int m, int n, int o) {
	a[k][l] = 2;
	int *iin = new int[8], *jin = new int[8], count = 0;
//	cout << k << ' ' << l << ' '<<m<<endl;

	fri(8)
		iin[i] = -1;
	fri(8)
		jin[i] = -1;
	if (l - 1 >= 0) {
		if (a[k][l - 1] == 0) {
			a[k][l - 1] = 1;
			iin[count] = k;
			jin[count++] = l - 1;
			m--;
		}
	}
	if (k - 1 >= 0) {
		if (a[k - 1][l] == 0) {
			a[k - 1][l] = 1;
			iin[count] = k - 1;
			jin[count++] = l;
			m--;
		}
	}
	if (l + 1 < o) {
		if (a[k][l + 1] == 0) {
			a[k][l + 1] = 1;
			iin[count] = k;
			jin[count++] = l + 1;
			m--;
		}
	}
	if (k + 1 < n) {
		if (a[k + 1][l] == 0) {
			a[k + 1][l] = 1;
			iin[count] = k + 1;
			jin[count++] = l;
			m--;
		}
	}
	if (k - 1 >= 0 && l - 1 >= 0) {
		if (a[k - 1][l - 1] == 0) {
			a[k - 1][l - 1] = 1;
			iin[count] = k - 1;
			jin[count++] = l - 1;
			m--;
		}
	}
	if (k + 1 < n && l - 1 >= 0) {
		if (a[k + 1][l - 1] == 0) {
			a[k + 1][l - 1] = 1;
			iin[count] = k + 1;
			jin[count++] = l - 1;
			m--;
		}
	}
	if (k - 1 >= 0 && l + 1 < o) {
		if (a[k - 1][l + 1] == 0) {
			a[k - 1][l + 1] = 1;
			iin[count] = k - 1;
			jin[count++] = l + 1;
			m--;
		}
	}

	if (k + 1 < n && l + 1 < o) {
		if (a[k + 1][l + 1] == 0) {
			a[k + 1][l + 1] = 1;
			iin[count] = k + 1;
			jin[count++] = l + 1;
			m--;
		}
	}

	if (m < 0) {
		fri(count)
			a[iin[i]][jin[i]] = 0;
		a[k][l] = 1;
		return false;
	} else if (m == 0) {
		return true; //return state todo
	} else {
		bool ans = false;
		fri(n)
		{
			frj(o)
			{
				if (a[i][j] == 1) {

					ans = traverse(a, i, j, m, n, o);
					if (ans)
						return ans;

				}
			}
		}
		fri(count)
			a[iin[i]][jin[i]] = 0;
		a[k][l] = 1;
		return ans;
	}
}
int main() {
	freopen("C-small-attempt2.in", "r", stdin);
	freopen("out.in", "w", stdout);
	int t;
	cin >> t;
	for (int t1 = 1; t1 <= t; t1++) {
		int r, c, m;
		cin >> r >> c >> m;
		m = r * c - m;
		int **a = new int *[r];
		fri(r)
		{
			a[i] = new int[c];
			frj(c)
				a[i][j] = 0;
		}
		bool ans = false;
		int ansi = 0, ansj = 0;
		if (m < 1)
			ansi = ansj = -1;
		fri(r)
		{
			frj(c)
			{
				if (m > 1) {
					a[i][j] = 2;
					m--;
					ans = traverse(a, i, j, m, r, c);
					m++;
					if (ans) {
						ansi = i;
						ansj = j;
						break;
					}
					a[i][j] = 0;
				} else
					ans = true;
			}
			if (ans)
				break;
		}
		cout << "Case #" << t1 << ": \n";
		if (ans) {
			fri(r)
			{
				frj(c)
				{
					if (i == ansi && j == ansj)
						cout << "c";
					else if (a[i][j] == 0)
						cout << "*";
					else
						cout << ".";
				}
				cout << endl;
			}
		} else
			cout << "Impossible\n";
	}
	return 0;
}
