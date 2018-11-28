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

using namespace std;

int main(){
	cin.sync_with_stdio(false);
	freopen ("A-large.in","r",stdin);
	freopen ("A-large.out","w",stdout);

	int T, smax, res, cur, si;
	string s;
	cin >> T;
	for(int t=1; t<=T; t++){
		res=0; cur=0;
		cin >> smax >> s;
		for(int i=0; i<=smax; i++){
			si=s[i]-48;
			if(i<=cur) cur+=si;
			else{
				res+=i-cur;
				cur+=si+i-cur;
			}
		}
		cout << "Case #" << t << ": " << res << endl;
	}
	return 0;
}