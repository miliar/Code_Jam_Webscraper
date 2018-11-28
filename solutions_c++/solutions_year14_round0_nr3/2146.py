#include<iostream>
#define fri(n) for(int i=0;i<n;i++)
#define frj(n) for(int j=0;j<n;j++)
using namespace std;
bool findans(int ** a, int k, int l, int m, int n, int o) {
	a[k][l] = 2;
	int *first = new int[8], *second = new int[8], count = 0;
	fri(8)
		first[i] = -1;
	fri(8)
		second[i] = -1;
	if (l - 1 >= 0) {
		if (a[k][l - 1] == 0) {
			a[k][l - 1] = 1;
			first[count] = k;
			second[count++] = l - 1;
			m--;
		}
	}
	if (k - 1 >= 0) {
		if (a[k - 1][l] == 0) {
			a[k - 1][l] = 1;
			first[count] = k - 1;
			second[count++] = l;
			m--;
		}
	}
	if (l + 1 < o) {
		if (a[k][l + 1] == 0) {
			a[k][l + 1] = 1;
			first[count] = k;
			second[count++] = l + 1;
			m--;
		}
	}
	if (k + 1 < n) {
		if (a[k + 1][l] == 0) {
			a[k + 1][l] = 1;
			first[count] = k + 1;
			second[count++] = l;
			m--;
		}
	}
	if (k - 1 >= 0 && l - 1 >= 0) {
		if (a[k - 1][l - 1] == 0) {
			a[k - 1][l - 1] = 1;
			first[count] = k - 1;
			second[count++] = l - 1;
			m--;
		}
	}
	if (k + 1 < n && l - 1 >= 0) {
		if (a[k + 1][l - 1] == 0) {
			a[k + 1][l - 1] = 1;
			first[count] = k + 1;
			second[count++] = l - 1;
			m--;
		}
	}
	if (k - 1 >= 0 && l + 1 < o) {
		if (a[k - 1][l + 1] == 0) {
			a[k - 1][l + 1] = 1;
			first[count] = k - 1;
			second[count++] = l + 1;
			m--;
		}
	}

	if (k + 1 < n && l + 1 < o) {
		if (a[k + 1][l + 1] == 0) {
			a[k + 1][l + 1] = 1;
			first[count] = k + 1;
			second[count++] = l + 1;
			m--;
		}
	}

	if (m < 0) {
		fri(count)
			a[first[i]][second[i]] = 0;
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

					ans = findans(a, i, j, m, n, o);
					if (ans)
						return ans;

				}
			}
		}
		fri(count)
			a[first[i]][second[i]] = 0;
		a[k][l] = 1;
		return ans;
	}
}
int main() {
	freopen("C-small-attempt1 (1).in", "r", stdin);
	freopen("out1.in", "w", stdout);
	int t;
	cin >> t;
	for (int caseno = 1; caseno <= t; caseno++) {
		int r, c, m;
		scanf("%d%d%d", &r, &c, &m);
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
					ans = findans(a, i, j, m, r, c);
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
		cout << "Case #" << caseno << ": \n";
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
