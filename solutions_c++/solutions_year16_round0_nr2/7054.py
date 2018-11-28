#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
using namespace std;
#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
typedef long long ll;
#define INF (1<<29)

int main(){
	int tc;
	string s;
	cin >> tc;
	for(int i=0;i<tc;i++){
		cin >> s;
		int ans=1;
		for(int j=1;j<s.length();j++)
			if(s[j]!=s[j-1])ans++;
		if(s[s.length()-1]=='+')ans--;
		cout << "Case #" << i+1 << ": " << ans << endl;
	}
	return 0;
}

