#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <deque>
#include <set>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <sstream>

#define For(i,a,n) for(int i =a ; i < n ; ++i )
#define all(x) (x).begin(),(x).end()
#define n(x) (int)(x).size()
#define pb(x) push_back(x)
#define fr first
#define sc second

using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
const int maxn = 2000+100;
int t;
int n;
int p[maxn];
int cost[maxn];


int main()
{
	ios::sync_with_stdio(false);
	cin >> t;
	For(it,0,t){
		cin >> n;
		For(i,0,n)
			cin >> p[i];


		int ans = maxn;

		For(ma,1,maxn){
			int ansl=ma;
			For(i,0,n)
				ansl+=(p[i]-1)/ma;
			ans=min(ans,ansl);
		}

		cout << "Case #" << it+1 << ": " << ans << endl;
	}
	return 0;
}

//
// el psy congroo
//

