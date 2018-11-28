
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

using namespace std;

int main()
{
	freopen("a.in", "r", stdin);
    freopen("b.out", "w", stdout);
	int tr; scanf( "%d", &tr );

	
	int a[100][100];
	int maxR[100], maxC[100];
	for(int kk =0 ; kk < tr; kk++){
		string ans = "YES";
	int n,m;
	scanf( "%d", &n );
	scanf( "%d", &m );

	int max1, max2;
	for(int i =0 ; i < n; i++){
		for(int j = 0; j < m ; j++)
			scanf( "%d", &a[i][j]);}

	int maximum;
	
	for(int x=0; x<n; ++x){maximum = 0;
		for(int y=0; y<m; ++y)maximum = std::max(a[x][y], maximum);		
		maxR[x] = maximum;}

	for(int x=0; x<m; ++x){maximum = 0;
		for(int y=0; y<n; ++y) maximum = std::max(a[y][x], maximum);		
		maxC[x] = maximum;}

	for(int i = 0; i < n; i++){
		for(int j =0 ; j < m; j++)
			if(a[i][j] != maxR[i] && a[i][j] != maxC[j])
			{ans = "NO";}}

	  cout<<"Case #"<<kk+1<<": "<<ans<<endl;
	}
	fclose (stdout);
	return 0;
}