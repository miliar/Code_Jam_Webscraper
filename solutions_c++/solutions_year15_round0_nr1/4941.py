	using namespace std;
#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i = (a), _b = (b); i <= _b; ++i)
#define FORD(i,a,b) for(int i = (a), _b = (b); i >= _b; --i)

int ntest, len, ans, c;
string s;

int main(){
	
	//freopen("A-small-attempt1.in","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("out","w",stdout);

	cin >> ntest;
	FOR(test,1,ntest){
		cin >> len >> s;
		ans = 0;
		c = 0;
		FOR(i,0,len){
			int p = s[i] - '0';
			if( i > c){
				ans += i - c;
				c = i;
			}
			c += p;
		}
		printf("Case #%d: %d\n",test,ans);
	}

	return 0;
}