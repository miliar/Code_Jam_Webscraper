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
#define LARGE 1

int main() {
#ifdef LARGE
	freopen("b_large.i", "rt", stdin);
	freopen("b_large.o", "wt", stdout);
#elif SMALL
	freopen("b_small.i", "rt", stdin);
	freopen("b_small.o", "wt", stdout);
#else
	freopen("b_sample.i", "rt", stdin);
#endif

	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++) {
		string s;
		cin>>s;
		int c=0;
		for(int i = 1; i < s.size(); c += (s[i] != s[i-1]), i++);
		cout << "Case #"<<tt<<": "<<c+(s.back() == '-')<<endl;
	}

	return 0;
}
