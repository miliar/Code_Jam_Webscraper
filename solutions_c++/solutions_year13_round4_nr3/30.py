#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <cstdio>

using namespace std;


int n;
vector <int> a, b;

bool les[2011][2011];



void Load()
{
	memset(les, 0, sizeof(les));
	cin >> n;
	a.resize(n);
	b.resize(n);
	int i;
	for (i= 0; i < n; i++) {
		cin >> a[i];
	}
	for (i= 0; i < n; i++) {
		cin >> b[i];
	}

}


int ans[2011];
int was[2011];
int time;



void Dfs(int v) 
{
	was[v] = 1;
	for (int i = n-1; i >= 0; i--) {
		if (les[v][i] && was[i] == 0)
			Dfs(i);
	}
	time++;
	ans[v] = n - time;
}


void Check()
{
	vector<int> aa(n, 1);
	vector<int> bb(n, 1);
	int i, j;
	for (i = 0; i < n; i++) {
		for (j = 0; j < i; j++) {
			if (ans[i] > ans[j] && aa[j] >= aa[i])
				aa[i] = aa[j] + 1;
		}
	}
	for (i = n-1; i >= 0; i--) {
		for (j = i+1; j < n; j++) {
			if (ans[i] > ans[j] && bb[j] >= bb[i])
				bb[i] = bb[j] + 1;
		}
	}
	for (i = 0; i < n; i++) {
		if (a[i] != aa[i]) cerr << "bad " << i << " got " << aa[i] << " expected " << a[i] << "\n";
		if (b[i] != bb[i]) cerr << "bad " << i << " got " << aa[i] << " expected " << a[i] << "\n";
	}
}

void Solve()
{
	int i, j;
	for (i = 0; i < n; i++) {
		bool foundprev = false;
		for (j = i-1; j >= 0; j--) {
			if (a[j] >= a[i])
				les[i][j] = true;
			if (a[j] == a[i] - 1 && !foundprev) {
				foundprev = true;
				les[j][i] = true;
			}
		}
		foundprev = false;
		for (j = i+1; j < n; j++) {
			if (b[j] >= b[i])
				les[i][j] = true;
			if (b[j] == b[i] - 1 && !foundprev) {
				foundprev = true;
				les[j][i] = true;
			}
		}
	}
	time = 0;
	memset(was, 0, sizeof(was));
	for (i = n-1; i >= 0; i--)
		if (was[i] == 0)
			Dfs(i);
	for (i = 0; i < n; i++) cout << ans[i]+1 << " ";
	cout << "\n";
	Check();
}

int main()
{
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++) {
		cout << "Case #" << tt << ": ";
		Load();
		Solve(); 
	}
	return 0;
}
