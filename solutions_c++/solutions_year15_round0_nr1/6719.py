#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;

#define f(i,n) for(i=0;i<n;++i)

int main() {
	freopen("gcj11.out","w",stdout);
	freopen("A-large.in","r",stdin);
	int n, t, i, m, sum, mor, tc = 0;
	string s;
	cin>>t;
	while (tc < t) {
		cin>>m>>s;
		sum = mor = 0;
		for(i=0;i<s.length();++i) {
			if (sum < i) {
				mor += i - sum;
				sum += i - sum;
			}
			sum += s[i] - '0';
		}
		cout<<"Case #"<<tc+1<<": "<<mor<<endl;
		++tc;
	}
}
