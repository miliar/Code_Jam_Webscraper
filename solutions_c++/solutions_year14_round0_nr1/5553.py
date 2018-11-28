#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <set>
#include <queue>
#include <deque>
#include <map>
#include <stack>
#include <string>
#include <sstream>
#include <vector>
#include <ctime>
#include <cstring>

#define ll long long
#define ld long double
#define vi vector<int>
#define vvi vector<vi >
#define pii pair<int,int>
#define pll pair<ll,ll>
#define vpii vector<pii >
#define vb vector<bool>
#define min(x,y) (x < y ? x : y)
#define min3(x,y,z) (min(x,min(y,z)))
#define max(x,y) (x > y ? x : y)
#define max3(x,y,z) (max(x,max(y,z)))
#define forn(i,n) for(int i = 0;i < n;i++)
#define sqrt(x) (pow(x,0.5))
#define sqr(x) (x * x)
#define mp make_pair
#define STDFILE 1
#define TASKNAME "xx"

const int inf = 1000 * 1000 * 1000;
const int mod = 1000 * 1000 * 1000 + 7;
const ld eps = 1e-9;

using namespace std;

int main(){
	freopen("INPUT.TXT","r",stdin);
	freopen("OUTPUT.TXT","w",stdout);
	int t;
	cin >> t;
	forn(i,t){
		cout << "Case #" << (i + 1) << ": ";
		int ans1,ans2;
		cin >> ans1;
		vi r(4),r2(4);
		forn(j,4){
			int p;
			if(j + 1 == ans1){
				forn(l,4)
					cin >> r[l];
			}
			else { 
				forn(l,4)
					cin >> p;
			}
		}
		cin >> ans2;
		forn(j,4){
			int p;
			if(j + 1 == ans2)
				forn(l,4)
				cin >> r2[l];
			else 
				forn(l,4)
				cin >> p;
		}
		int ans = -1;
		bool c = true;
		forn(j,4){
			forn(l,4){
				if(r[j] == r2[l]){
					if(ans != -1){
						cout << "Bad magician!" << endl;
						c = false;
					}
					else ans = r[j];
				}
				if(!c)
					break;
			}
			if(!c)
				break;
		}
		if(!c)
			continue;
		if(ans == -1)
				cout << "Volunteer cheated!" << endl;
		else cout << ans << endl;
	}
	return 0;
}