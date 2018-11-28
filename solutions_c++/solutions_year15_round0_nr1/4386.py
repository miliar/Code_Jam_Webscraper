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
#include <climits>
#include <string>
#include <cstring>
#include <cassert>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for (int T = 1; T <= t; ++T) {
		int Smax;
		string S;
		cin>>Smax;
		cin>>S;
		int curr=(S[0]-'0'),ans=0;
		for (int i = 1; i < S.size(); ++i) {
			if(curr<i) {
				ans+=(i-curr);
				curr+=(i-curr);
			}
			curr+=(S[i]-'0');
		}
		printf("Case #%d: %d\n",T,ans);
	}
	return 0;
}