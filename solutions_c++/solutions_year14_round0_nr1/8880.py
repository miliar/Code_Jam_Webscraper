#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <sstream>
#include <numeric>
#include <functional>
#include <string>
#include <cstring>
#include <stack>
#include <queue>

#define vi vector<int>
#define vvi vector< vectort<int> >
#define pii pair<int, int>
#define vpii vector<pii>
#define mii map<int, int>
#define rep(i, n) for(int i = 0; i < (n); ++i)
#define f(i, a, b) for(int i =(a); i < (b); ++i)
#define fd(i, a, b) for(int i = (a); i >= (b); --i)
// #define prv(v) for(typeof(int) i = 0; i < sizeof(v)/sizeof(*v); ++i) cout << *(v+i) << " "; cout<<endl
#define prv(v) for(auto i = 0; i < sizeof(v)/sizeof(*v); ++i) cout << *(v+i) << " "; cout<<endl

// #define fc(it, c) for(typeof((c).begin()) it = (c).begin(); it!=(c).end(); it++)
#define fc(it, c) for(auto it = (c).begin(); it!=(c).end(); it++)
#define prc(c) for(auto i = (c).begin(); i !=(c).end(); i++ ) cout << *i << " "; cout<<endl
// #define prc(c) for(typeof((c).begin()) i = (c).begin(); i !=(c).end(); i++ ) cout << *i << " "; cout<<endl
#define all(c) (c).begin(), (c).end()
#define allr(c) (c).rbegin(), (c).rend()
#define present(c, e) ((c).find(e) != (c).end())//set/map,etc
#define presentc(c, e) ((c).find(all(c), e) != (c).end())//vector

typedef long long ll;
#define szc(c) int((c).size())
#define szv(v) sizeof(v)/sizeof(v[0])
#define pb(x) push_back(x)
#define print(x) cout << x << endl

#define MAX(x, y) (((x) > (y)) ? (x) : (y))
#define MIN(x, y) (((x) < (y)) ? (x) : (y))
using namespace std;

long long mod = 1e9 + 7;

int main(int argc, const char *argv[])
{
	freopen("A-small-attempt2.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n = 4;
	int cards[n][n];
	int cards2[n][n];
	int array[n];
	int T;
	int row1;
	int row2;
	cin >> T;
	f(k, 1, T+1) {
		cin >> row1;	
		f(i, 0, n) {
			f(j, 0, n) {
				scanf("%d", &cards[i][j]);
			}
		}
		f(i, 0, n) {
			array[i] = cards[row1-1][i];

		}
		set<int> s(array, array + n);

		cin >> row2;	
		f(i, 0, n) {
			f(j, 0, n) {
				scanf("%d", &cards2[i][j]);
			}
		}

		int flag;
// 		f(i, 0, n) {
// 			flag = 0;
// 			f(j, 0, n) {
// 				if(array[j] == cards2[j][i])
// 					flag++ ;
// 			}
// 			if(flag == 4) break;
// 		}
		int badMagician = 0;
		int key;
		f(i, 0, n){
			if(present(s, cards2[row2-1][i])) {
				badMagician++;
				key = cards2[row2-1][i];
			}
		}
		if(badMagician == 1)
			printf("Case #%d: %d\n", k, key);
		else if(badMagician > 1)
			printf("Case #%d: Bad magician!\n", k);
		else if(badMagician == 0){
			printf("Case #%d: Volunteer cheated!\n", k);

		}

	}

	return 0;
}

