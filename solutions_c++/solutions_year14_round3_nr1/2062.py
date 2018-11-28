#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define INF (1<<29)
#define EPS (1e-10)
#define make_pair mp
#define pb push_bacck

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef pair<int,int> pii;

int dx[] = {0,1,0,-1}, dy[] = {1,0,-1,0};

int main(){
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		int p, q;
		scanf("%d/%d", &p, &q);
		double np = (double)p / (double)q;
		set<int> data;
		data.insert(np);
		bool exist = false;
		long long ans = -1;
		for (long long j = 1; j <= 32 ; j++) {
			//cout << np << endl;
			np *= 2.0;
			if (1.0 <= np) {
				if (ans == -1) ans = j;
				np -= 1.0;
				if (np == 0) {
					exist = true;
					break;
				}
			}
			//set<double>::iterator p = data.begin();
			//for ( ; p != data.end(); p++) cout << *p << endl;
			/*if (data.find(np) == data.end()) data.insert(np);
			else {
				exist = false;
				break;
			}
			*/
		}
		if (exist) cout << "Case #" << i << ": " << ans << endl;
		else cout << "Case #" << i << ": impossible" << endl;
	}
}
