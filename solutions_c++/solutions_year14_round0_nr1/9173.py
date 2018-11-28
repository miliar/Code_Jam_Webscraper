#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <bitset>
#include <deque>
#include <iostream>
#include <iomanip>
#include <limits>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;
typedef vector <int> vi;
typedef vector <string> vs;
typedef istringstream iss;
typedef ostringstream oss;

int a[10][10] = {0};
int b[10][10] = {0};

int main(){
	#ifndef ONLINE_JUDGE
 		freopen("A-small-attempt1.in", "r", stdin);
		freopen("A-small-attempt1.out", "w", stdout);
	#endif
	ios_base::sync_with_stdio(false);
	int t;
	
	int d[20] = {0};
	string s1 = "Bad magician!";
	string s2 = "Volunteer cheated!";
	cin >> t;
	int n = t;
	for(int k = 0; k < t; k++){
		int x, y;
		int d[20] = {0};
		cin >> x;
		for(int i =1; i <= 4; i++){
			for(int j = 1; j <= 4; j++){
				cin >>a[i][j];
			}
		}
		cin >> y;
		for(int i = 1; i < 5; i++) d[a[x][i]] = 1;
		for(int i =1; i <= 4; i++){
			for(int j = 1; j <= 4; j++){
				cin >>b[i][j];
			}
		}
		int cnt = 0, lx = 0;	
		for(int i =1; i <5; i++)
			if (d[b[y][i]] == 1) {
				cnt++;
				lx = b[y][i];
			}	
		cout << "Case #" <<  k+1 <<  ": ";
		if (cnt == 0)  cout << s2 << endl;
		else 
			if (cnt == 1) cout << lx << endl;
			else cout << s1 << endl;
	}
	return 0;
}



