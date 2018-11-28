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
#include<algorithm>
#include<iterator>
#include<numeric>
using namespace std;

#define SMALL 1
//#define LARGE 1

int main() {
#ifdef LARGE
	freopen("d_large.i", "rt", stdin);
	freopen("d_large.o", "wt", stdout);
#elif SMALL
	freopen("d_small.i", "rt", stdin);
	freopen("d_small.o", "wt", stdout);
#else
	freopen("d_sample.i", "rt", stdin);
#endif

	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++) {
		int k,c,s;
		cin>>k>>c>>s;
		cout<<"Case #"<<tt<<":";
		if((c == 1 && s != k) || (c > 1 && s < (k+1)/2)) {
			cout << " IMPOSSIBLE" << endl;
			continue;
		}
		if (c == 1) {
			for (int i=1;i<=k;i++)
				cout << " " << i;
			cout << endl;
			continue;
		}
		int off = 0, st = 2;
		for (int i = 0; i < k/2; off+=2*k, st+=2, i++) {
			cout << " " << off+st;
		}
		if (k%2)
			cout << " " << k;
		cout<<endl;
	}

	return 0;
}
