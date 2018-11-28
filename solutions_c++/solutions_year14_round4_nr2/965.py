//be name oo
#include <algorithm>
#include <iostream>
#include <fstream>
#include <map>
#include <utility>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <sstream>
#include <set>
#include <complex>
#include <iomanip>
#include <queue>

#define FOR(i, n) for(int i = 0; i < (n); i++)
#define SZ(x) ((int)x.size())
#define PB push_back
#define show(x) cerr << "#" << #x << ": " << x << endl
#define F first
#define S second
#define X real()
#define Y imag()

using namespace std;
typedef pair<int, int> pii;
typedef complex<double> point;

const int MAX_N = 1000 + 10;

int n;
int num[MAX_N];

int main(){
	int num_test_case;
	cin >> num_test_case;
	for(int _test = 1; _test <= num_test_case; _test++){
		cout << "Case #" << _test << ": ";
		cin >> n;
		FOR(i, n)
			cin >> num[i];
		int ans = 0;
		FOR(i, n){
			int left = 0, right = 0;
			FOR(j, i)
				if(num[j] > num[i])
					left++;
			for(int j = i + 1; j < n; j++)
				if(num[j] > num[i])
					right++;
			ans += min(left, right);
		}	
		cout << ans << endl;
	}
	return 0;
}

