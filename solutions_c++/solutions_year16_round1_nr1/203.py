#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <sstream>
#include <functional>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <list>
#include <numeric>
using namespace std;
const double PI = 3.14159265358979323846;
const double EPS = 1e-12;
const int INF = 1<<25;
typedef pair<int,int> P;
typedef long long ll;
typedef unsigned long long ull;


int main(){
	int T;
	cin>>T;
	for(int Case = 1; Case <= T; Case++){
		string s;
		cin>>s;
		string t;
		t += s[0];
		int n = s.size();
		for(int i = 1; i < n; i++){
			if(s[i]>=t[0]) t = s.substr(i, 1)+t;
			else t = t+s.substr(i, 1);
		}
		printf("Case #%d: %s\n", Case, t.c_str());
	}
	return 0;
}

