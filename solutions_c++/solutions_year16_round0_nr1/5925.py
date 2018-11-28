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

//#define SMALL 1
#define LARGE 1

void mark(long long n, vector<int>& v) {
	if(n==0) {
		v[0] = 1;
		return;
	}
	while(n>0) {
		v[n%10] = 1;
		n/=10;
	}
}

int main() {
#ifdef LARGE
	freopen("a_large.i", "rt", stdin);
	freopen("a_large.o", "wt", stdout);
#elif SMALL
	freopen("a_small.i", "rt", stdin);
	freopen("a_small.o", "wt", stdout);
#else
	freopen("a_sample.i", "rt", stdin);
#endif

	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++) {
		long long n,nn;
		cin>>n;
		vector<int> v(10);
		if(n == 0) {
			cout<<"Case #"<<tt<<": INSOMNIA"<<endl;
			continue;
		}
		for(nn=n; accumulate(v.begin(), v.end(), 0, plus<int>()) < 10; nn+=n) {
			mark(nn, v);
		}
		cout<<"Case #"<<tt<<": "<<nn-n<<endl;
	}

	return 0;
}
