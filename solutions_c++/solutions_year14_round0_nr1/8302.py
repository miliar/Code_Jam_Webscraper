#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <fstream>
#include <ctime>
#include <climits>
#include <bitset>
#include <cmath>
#include <tr1/unordered_map>
#include <tr1/unordered_set>
 
#define FOR(i,f,t) for(int i = f;i<t;i++)
#define For(i, t) for(int i = 0;i<t;i++)
#define ITER(it, a) for(typeof (a.begin()) it = a.begin();it != a.end();it++)
#define range(cont) cont.begin(), cont.end()
#define mp(i,j) make_pair(i,j)
#define pb push_back
#define inf 10737418

using namespace std;
using namespace std::tr1;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<pii> vpii;

int main(){

	int nc;
	scanf("%d", &nc);

	For(i, nc){
		set<int> f;
		int tip, t;
		scanf("%d", &tip);
		For(j, 4*(tip-1))
			scanf("%d", &t);

		For(j, 4){
			scanf("%d", &t);
			f.insert(t);
		}

		For(j, 4*(4 - tip))
			scanf("%d", &t);

		int tot = 0, ans;

		scanf("%d", &tip);
		For(j, 4*(tip-1))
			scanf("%d", &t);

		For(j, 4){
			scanf("%d", &t);
			if(f.count(t)){tot++;ans = t;}
		}

		For(j, 4*(4 - tip))
			scanf("%d", &t);

		if(!tot)
			printf("Case #%d: Volunteer cheated!\n", i+1);
		else if(tot == 1)
			printf("Case #%d: %d\n", i+1, ans);
		else 
			printf("Case #%d: Bad magician!\n", i+1);
	}
	return 0;
}