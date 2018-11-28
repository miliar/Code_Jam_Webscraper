#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <algorithm>
#include <cctype>
#include <ctime>
#include <cmath>
#include <iomanip>
#include <cassert>
                   
using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++) 
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = int(a); i < int(b); i++)

#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define X first
#define Y second

typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long long ll;
typedef long double ld;
typedef double ldd;

const int INF = 1E9;   
const ld eps = 1e-6;
const ld pi = acos(-1.0);
const int MAXN = 111111;   
const ll MOD = 1E9 + 7;
                         
int tt, k[2], matches, id;
int a[2][4][4];

int main() {

    cin >> tt;
    forn(t, tt) {
    	printf("Case #%d: ", t + 1);
    	forn(i, 2) {
    		cin >> k[i];
    		k[i]--;
    		forn(j, 4)
    			forn(l, 4)
    				cin >> a[i][j][l];
    	}

    	matches = 0;
    	forn(i, 4) {
    		forn(j, 4)
    			if (a[0][k[0]][i] == a[1][k[1]][j]) {
    				matches++;
    				id = a[0][k[0]][i];
    			}
    	}

    	if (matches > 1)
    		cout << "Bad magician!";
    	else if (matches == 1) 
    		cout << id;
    	else
    		cout << "Volunteer cheated!";
    	cout << '\n';
    }
	
    return 0;
}