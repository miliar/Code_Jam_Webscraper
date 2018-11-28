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
double a[MAX_N];
double b[MAX_N];

int main(){
	int num_test_case;
	cin >> num_test_case;
	for(int _test = 1; _test <= num_test_case; _test++){
		cout << "Case #" << _test << ": ";

		cin >> n;
		FOR(i, n)
			cin >> a[i];
		FOR(i, n)
			cin >> b[i];
		sort(a, a + n);
		sort(b, b + n);

		set<double> nam(a, a + n), ken(b, b + n);
		int points = 0;
		FOR(i, n){
			double choose_nam = *nam.rbegin();
			double choose_ken = *ken.rbegin();
			if(choose_nam > choose_ken){
				points++;
				nam.erase(nam.upper_bound(*ken.begin()));
				ken.erase(*ken.begin());
			}else{
				nam.erase(nam.begin());
				ken.erase(choose_ken);
			}
		}
		cout << points << " ";

		nam = set<double>(a, a + n);
		ken = set<double>(b, b + n);
		points = 0;
		FOR(i, n){
			double choose_nam = *nam.rbegin();
			if(ken.upper_bound(choose_nam) == ken.end()){
				points++;
				nam.erase(choose_nam);
				ken.erase(*ken.begin());
			}else{
				nam.erase(choose_nam);
				ken.erase(ken.upper_bound(choose_nam));
			}
		}
		cout << points << endl;
	}
	return 0;
}

