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

#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
typedef long long ll;  
#define FOR(i,n) for (int i = 0; i < n; i++)
#define SZ(x) ((int)x.size())
#define PB push_back
#define split(str) {vs.clear();istringstream ss(str);while(ss>>(str))vs.push_back(str);}
using namespace std;

int main()
{
	int t;
	scanf("%d", &t);
	FOR(case1, t)
	{
		int n;
		cin >> n;
		vector<double> bandi, banda;
		FOR(i, n)
		{
			double x;
			cin >> x;
			bandi.PB(x);
		}
		FOR(i, n)
		{
			double x;
			cin >> x;
			banda.PB(x);
		}
		sort(all(bandi));
		sort(all(banda));
		reverse(all(bandi));
		reverse(all(banda));

		int ans1 = 0;
		int j = 0;
		FOR(i, n)
			if(banda[j] > bandi[i])
			{
				ans1++;
				j++;
			}
		//reverse(all(bandi));
		ans1 = n - ans1;

		reverse(all(bandi));
		reverse(all(banda));

		int ans2 = 0;
		j = 0;
		FOR(i, n)
		{
			//cout << bandi[i] << " " << banda[j] << endl;
			if(bandi[i] > banda[j])
			{
				ans2++;
				j++;
			}
		}
		cout << "Case #" << (case1 + 1) << ": " << ans2 << " " << ans1 << endl;
	}
}