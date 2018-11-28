										/* in the name of Allah */
#include <algorithm>
#include <iostream>
#include <memory.h>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <list>
#include <map>
#include <set>

using namespace std;

#define uint unsigned int
#define int64 long long
#define P pair<double, double>
#define Pss pair<string, string>
#define PLL pair<int64, int64>
#define Inf 1000000
#define Mod 1000000007LL
#define eps 1e-9

int n;
double V, temp;
P arr[110];

bool eq(double a, double b){
	return fabs(a - b) < eps;
}

bool ls(double a, double b){
	return a + eps < b;
}

int main(){
	freopen("B. Kiddie Pool.in", "r", stdin);
	freopen("B. Kiddie Pool.out", "w", stdout);
	int T, test = 0;
	for(cin >> T; T--; ){
		cin >> n >> V >> temp;
		for(int i = 0; i < n; i++)
			cin >> arr[i].second >> arr[i].first;
		sort(arr, arr + n);
		cout << "Case #" << ++test << ": ";

		if(n == 1){
			if(!eq(temp, arr[0].first))
				cout << "IMPOSSIBLE" << endl;
			else cout << setprecision(9) << fixed << V / arr[0].second << endl;
			continue;
		}
		
		if(ls(arr[0].first, temp) && ls(arr[1].first, temp)){
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		if(ls(temp, arr[0].first) && ls(temp, arr[1].first)){
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		if(eq(temp, arr[0].first) && eq(temp, arr[1].first)){
			cout << setprecision(9) << fixed << V / (arr[0].second + arr[1].second) << endl;
			continue;
		}
		if(eq(temp, arr[0].first)){
			cout << setprecision(9) << fixed << V / (arr[0].second) << endl;
			continue;
		}
		if(eq(temp, arr[1].first)){
			cout << setprecision(9) << fixed << V / (arr[1].second) << endl;
			continue;
		}
		double diff = arr[1].first - arr[0].first;
		double n1 = V * (temp - arr[0].first) / diff;
		double n0 = V * (arr[1].first - temp) / diff;
		cout << setprecision(9) << fixed << max(n0 / arr[0].second, n1 / arr[1].second) << endl;
	}
	return 0;
}
