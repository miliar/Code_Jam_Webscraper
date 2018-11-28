#include <iostream>
#include <fstream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <iomanip>
using namespace std;
#define MAX 200020
#define VMAX 260
int t, cnt(0);
double c, f, x;
double tim(0), speed[MAX], cost[MAX], wat[MAX], ans[MAX];
ifstream fin("B-large.in");
void solve();
int main()
{
	cin.rdbuf(fin.rdbuf());
	cin >> t;
	while(t --){
		cin >> c >> f >> x;
		solve();
	}
}
void solve()
{
	memset(speed, 0, MAX * sizeof(double));
	memset(wat, 0, MAX * sizeof(double));
	memset(cost, 0, MAX * sizeof(double));
	speed[0] = 2; wat[0] = 0; cost[0] = x / speed[0];
	for(int i = 1; i < MAX; ++ i){
		wat[i] = wat[i - 1] + c / speed[i - 1];
		speed[i] += speed[i - 1] + f;
		cost[i] = x / speed[i];
	}
	double ans = cost[0];
	for(int i = 1; i < MAX; ++ i)
		ans = min(ans, cost[i] + wat[i]);
	cout << "Case #" << ++ cnt << ": " << setiosflags(ios::fixed) << setprecision(7) << ans << endl; 
}


