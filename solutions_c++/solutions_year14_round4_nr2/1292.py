//In the Name of Allah
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
//#include <algorithm>
using namespace std;

const double eps = 1e-12;
typedef long long ll;
typedef pair<int, int> pii;
//#define For(i, a, b) for (int i = (a); i < (b); i++)
#define debug(x) { cerr << #x << " = _" << (x) << "_" << endl; }
void Error(string err) { cout << err; cerr << err; while(1); }
/************************************************************************/

int n;
int temp[100];

int cmp (const int arr[], const int v[]) {

	for (int i=0; i<n; i++) temp[i] = arr[i];
	int ret = 0;
	for (int i=0; i<n; i++){
		int j = i;
		for (;;j++){
			if(temp[j] == v[i]) break;
		}
		ret += j-i;
		for (; j>i; j--)
			temp[j] = temp[j-1];
	}
	return ret;
}

int cnt;
map <int, bool> mp;
int v[100];

bool prom (int ind) {
	int i=0;
	while(i < ind-1 && v[i] < v[i+1]) i++;
	if (i == ind-1) return true;
	while(i < ind-1 && v[i] > v[i+1]) i++;
	if (i == ind-1) return true;
	return false;
}
void f (int ind, const int arr[]) {
	if (ind > 2 && !prom(ind)) return;
	if (ind == n) {
		cnt = min(cnt, cmp(arr, v));
		return;
	}
	for (int i=0; i<n; i++){
		if(mp[arr[i]]) continue;
		mp[arr[i]] = true;
		v[ind] = arr[i];
		f (ind+1, arr);
		mp[arr[i]] = false;
	}
}

int main () {
	//*
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	//*/
	int arr[100];
	int T;
	cin >> T;
	for(int tc=1; tc<=T; tc++){
		debug(tc);
		cin >> n;
		mp.clear();
		for (int i=0; i<n; i++){
			cin >> arr[i];
			mp[arr[i]] = false;
		}
		cnt = n*n*n;
		f(0, arr);
		cout << "Case #" << tc << ": " << cnt << endl;;
	}
	return 0;
}
/*
?
10 _0 am 8 7 6 5
10 5 2 am 6 4 1

6
3
1 2 3
5
1 8 10 3 7
6
1 2 3 4 5 0
6
1 2 3 4 5 6
6
8 7 6 5 4 9
6
9 2 3 4 5 6

0
1
0
0
5 - 4
5 - 4
*/