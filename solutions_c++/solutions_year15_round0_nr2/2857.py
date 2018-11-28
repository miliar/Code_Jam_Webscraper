#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<string.h>
#include<cmath>
using namespace std;

//#define SMALL 1
#define LARGE 1

int main() {
#ifdef LARGE
	freopen("b_large.i", "rt", stdin);
	freopen("b_large.o", "wt", stdout);
#elif SMALL
	freopen("b_small_2.i", "rt", stdin);
	freopen("b_small_2.o", "wt", stdout);
#else
	freopen("b_sample.i", "rt", stdin);
#endif

	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++) {
		int n;
		cin>>n;
		vector<int> v(n);
		for (int i=0;i<n;i++)
			cin>>v[i];
		sort(v.begin(), v.end());
		int ans = 10000;
		for(int i=1;i<=v[n-1];i++) {
			int cur = 0;
			for(int j=0;j<n;j++) {
				if (v[j] <= i)
					continue;
				cur += ((v[j]+i-1) / i) - 1;
			}
			ans = min(ans, cur+i);
		}
		cout<<"Case #"<<tt<<": "<<ans<<endl;
	}

	return 0;
}
