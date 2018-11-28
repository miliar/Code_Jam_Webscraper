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


int a, b;
int t[1001];
void Load()
{
	cin >> a >> b;
}

void Solve()
{
	cout << t[b] - t[a-1] << "\n";
}

int main()
{
	int nt, tt;
	t[1] = t[4] = t[9] = t[121] = t[484] = 1;
	int i;
	for (i = 1; i <= 1000; i++) t[i] += t[i-1];
	cin >> nt;
	for (tt = 1; tt <= nt; tt++) {
		cout << "Case #" << tt << ": ";
		Load();
		Solve(); 
	}
	return 0;
}
