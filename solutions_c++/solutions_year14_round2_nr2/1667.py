#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
using namespace std;


#define REP(i,n) for(int i=0; i<n; i++)
#define REPs(i,x,n) for(int i=x; i<n; i++)
#define SZ(x) x.size()
#define VVII vector< vector< pair<int, int> > > 
#define mem(f, a) memset(f, a, sizeof(f))
#define all(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair
#define epsil 1e-9
#define infinit  1e8
#define ll long long
#define PI pair<int, int>
#define X first
#define Y second

//bool A[1000];

int main()
{
	ifstream cin("B-small-attempt0.in");
	ofstream cout("out.txt");
	int t; cin >> t;
	//TODO special case when impossible!
	REP(i, t){
		cout << "Case #" << i + 1 << ": ";
		int A, B, K;
		int ans = 0;
		cin >> A >> B >> K;
		REP(i, A) REP(j, B){
			if ((i & j) < K) ans++;
		}
		cout << ans<<endl;
	}
	return 0;
}