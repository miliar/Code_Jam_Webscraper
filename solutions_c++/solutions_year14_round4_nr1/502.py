#include <iostream>
#include <iomanip>
#include <cstdio>
#include <math.h>
#include <algorithm>
#include <queue>
#include <string>
#include <fstream>
#include <vector>
#include <stack>
#include <map>
#include <set>
#include <ctime>
#include <iomanip>

#define all(x) (x).begin(), (x).end()
#define pb push_back
#define double long double
#define LL long long
#define itn int

using namespace std;

int main(){

	int T;
	cin >> T;
	for (int _ = 0; _ < T; _++){
		cout << "Case #" << _ + 1 << ": ";
		int n, x;
		cin >> n >> x;
		vector<int> a(n);
		for (int i = 0; i < n; i++) cin >> a[i];
		int s = 0;
		sort(all(a));
		int j = 0;
		for (int i = n - 1; i >= j; i--){
			if (a[i] + a[j] <= x) j++;
			s++;
		}
		cout << s << "\n";
	}

	return 0;
	
}