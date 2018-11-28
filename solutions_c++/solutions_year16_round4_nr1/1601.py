#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <list>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <set>
#include <utility>
#include <stack>

#define rep(i,n) for(int i = 0; i < (int)(n); i++)

using namespace std;

void solve();
void runCase();

bool go(string s,int n) {
	int len = 1<<n;
	for(int i = 0; i < n; i++) {
		for(int j = 0, k = 0;j < len; j+=2) {
			if((s[j]=='R' && s[j+1]=='P')
			|| (s[j]=='P' && s[j+1]=='R')) {
				s[k++] = 'P';
			} else
			if((s[j]=='S' && s[j+1]=='P')
			|| (s[j]=='P' && s[j+1]=='S')) {
				s[k++] = 'S';
			} else 
			if((s[j]=='R' && s[j+1]=='S')
			|| (s[j]=='S' && s[j+1]=='R')) {
				s[k++] = 'R';
			} else 
			if(s[j]==s[j+1]) return false;
		}
		len >>= 1;
	}
	return true;
}

void runCase()
{
	int N,R,P,S;
	cin >> N >> R >> P >> S;
	string s;
	s = string(R,'R');
	s += string(P,'P');
	s += string(S,'S');
	
	int f = 0;
	sort(s.begin(),s.end());
	do {
		if(go(s,N)) {
			f = 1;
			break;
		}
	} while( next_permutation(s.begin(),s.end()) );
	if(f) cout << s << endl;
	else cout << "IMPOSSIBLE" << endl;
}

void solve()
{
	int n;
	cin >> n;
	// scanf("%d",&n);
	// getchar();

	for(int i = 0; i < n; i++) {
        	cout << "Case #" << i+1 << ": ";
		// printf("Case #%d: ",i+1);
		runCase();
		//runSample();
	}
}

int main()
{
	ios::sync_with_stdio(false); cin.tie(0);
	solve();
	return 0;
}
