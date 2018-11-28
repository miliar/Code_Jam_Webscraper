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
#define mp make_pair
#define double long double
#define LL long long
#define itn int

using namespace std;

int main(){

	int T;
	cin >> T;
	for (int _ = 0; _ < T; _++){
		cout << "Case #" << _ + 1 << ": ";
		int n;
		cin >> n;
		vector<int> a(n);
		for (int i = 0; i < n; i++){
			cin >> a[i];
		}
		int s = 0;
		vector<pair<int, int> > ar(n);
		for (int i = 0; i < n; i++) ar[i] = mp(a[i], i);
		sort(all(ar));
		vector<int> fenv(n, 0);
		for (int i = 0; i < n; i++){
			int ind = ar[i].second;
			int j = ind;
			while (j >= 0){
				ind -= fenv[j];
				j = (j & (j + 1)) - 1;
			}
			s += min(ind, n - 1 - i - ind);
			j = ar[i].second;
			while (j < n){
				fenv[j]++;
				j = (j | (j + 1));
			}
		}
		cout << s << "\n";
	}

	return 0;
	
}