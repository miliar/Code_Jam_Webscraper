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
#include <cstring>

#define lld long long int 
#define EOL '\0'

#define N 102
#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define rep(n) for(int i =0;(i)<(int)(n);(i)++)
#define repi(n) for(int i =0;(i)<(int)(n);(i)++)
#define repj(n) for(int j =0;(j)<(int)(n);(j)++)
#define repij(n,m) for(int i =0;(i)<(int)(n);(i)++) for(int j =0;(j)<(int)(m);(j)++)

using namespace std;

int f[N][N];
int rmax[N],cmax[N];

string solve() { 
	int n,m;
	cin>>n>>m;
	rep(N) rmax[i]=0,cmax[i]=0;
	repij(n,m) 
		cin>>f[i][j],
		rmax[i] = (rmax[i] < f[i][j] ) ? f[i][j] : rmax[i],
		cmax[j] = (cmax[j] < f[i][j] ) ? f[i][j] : cmax[j];
		
	repij(n,m)
		if(f[i][j] != rmax[i] && f[i][j]!= cmax[j])
			return "NO";
	return "YES";
}


int main() 
{
	int n;
	freopen("C:\\MyCode\\jam\\Data\\B-large.in", "r",stdin);
	freopen("C:\\MyCode\\jam\\Data\\B-large.out", "w",stdout);
	cin>>n;string s;
	rep(n) 
		cout<<"Case #"<<i+1<<": "<<solve()<<endl;
	return 0;
}