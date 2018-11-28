#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cctype>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <complex>
using namespace std;

typedef long long ll;
typedef unsigned long long llu;
typedef long double ld;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef stringstream ss;

ll ans()
{
ll ml,dis,cnt=0;
cin >> dis;
cin >> ml;
while(ml>=(2*dis+1))
	{
		ml-=2*dis+1;
		dis+=2;
		cnt++;
	}	
	return cnt;
}

int main()
{
	int i,n;
	cin >> n;
	for(i=0;i<n;i++)
		{
			cout << "Case #" << i+1 << ": " << ans() << endl;
		}
	return 0;
}
