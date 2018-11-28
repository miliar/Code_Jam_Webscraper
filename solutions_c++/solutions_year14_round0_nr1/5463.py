#pragma comment(linker, "/STACK:16777216")
#include <vector>
#include <string>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <map>
#include <queue>
#include <set>
#include <memory.h>
#include <string.h>
#include <deque>
#include <assert.h>
#include <stack>
using namespace std;

#define FOR(i,a,b) for(int (i) = (a); (i) <= (b); ++(i))
#define inf 2000000000
#define pb push_back
#define all(c) (c).begin(), (c).end()
#define pi 2*acos(0.0)
#define mp(a,b) make_pair((a), (b))
#define X first
#define Y second

typedef vector<int> vint;
typedef long long ll;
typedef pair<int, int> pii;

int t;
int a,b;
int card1[5][5];
int card2[5][5];
int used[17];

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> t;
	FOR(tt, 1, t){
		memset(used, 0, sizeof(used));
		cin >> a;
		FOR(i,1,4){
			FOR(j,1,4){
				cin >> card1[i][j];
				if(i == a){
					used[card1[i][j]]++;
				}
			}
		}
		cin >> b;
		FOR(i,1,4){
			FOR(j,1,4){
				cin >> card2[i][j];
				if(b == i){
					used[card2[i][j]]++;
				}
			}
		}

		int ans = 0;
		FOR(i,1,16){
			if(used[i] >= 2){
				if(ans == 0){
					ans = i;
				}else{
					ans = -1;
				}
			}
		}
		if(ans == 0){
			cout << "Case #" << tt << ": " << "Volunteer cheated!" << endl;
		}else if(ans == -1){
			cout << "Case #" << tt << ": " << "Bad magician!" << endl;
		}else{
			cout << "Case #" << tt << ": " << ans << endl;
		}


	}
	
	
	
	
    return 0;
}