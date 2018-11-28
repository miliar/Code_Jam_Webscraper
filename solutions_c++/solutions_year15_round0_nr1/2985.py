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
		int n;
		string s;
		cin>>n>>s;
		int cnt = 0;
		int sum = 0;
		for(int i=0;i<s.size();i++) {
			if (s[i] > '0')
				cnt += max(i-cnt, 0);
			cnt+=s[i]-'0';
			sum += s[i]-'0';
		}
		cout << "Case #"<<tt<<": "<<cnt-sum<<endl;
	}

	return 0;
}
