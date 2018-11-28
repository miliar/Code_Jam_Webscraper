#include <cstdio>
#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>
#include <cmath>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <stack>
 
using namespace std;

void solve()
{
	int n; cin >> n; vector<int> a(n); for(int i=0; i<n; ++i) cin>>a[i];
	
	int l = 0, r = n, cnt = 0;
	for(int i=0; i<n; ++i)
	{
		int index = min_element(a.begin()+l, a.begin()+r) - a.begin();
		int dl = index - l, dr = r - index - 1;

		if(dl<dr)
		{
			++l; while(index && a[index]<a[index-1]){swap(a[index], a[index-1]); --index; ++cnt;}
		}
		else
		{
			--r; while(index<n-1 && a[index]<a[index+1]){swap(a[index], a[index+1]); ++index; ++cnt; }
		}
	}
	cout<<cnt<<endl;
}

int main()
{
#ifdef GRANDVIC_DEBUG
	//freopen("i:/input.txt", "rt", stdin);
#endif
	ios_base::sync_with_stdio(0);
	int T; cin>>T;
	for(int t=1; t<=T; ++t)
	{
		cout << "Case #" << t << ": ";
		solve();
	}
	return 0;
} 