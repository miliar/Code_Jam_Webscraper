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
	int tc, sm;
	string s;
	cin >> tc;
	for(int i=0;i<tc;i++){
		cin >> sm >> s;
		int cnt=s[0]-'0', ans=0;
		for(int j=1;j<=sm;j++){
			if(j>cnt){
				ans++;
				cnt++;
			}
			cnt+=s[j]-'0';
		}
		cout << "Case #" << i+1 << ": " << ans << endl;
	} 
	return 0;
}

