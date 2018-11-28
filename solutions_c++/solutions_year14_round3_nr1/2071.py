#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <sstream>

typedef long long int li;
typedef long long int lli;

#define F(i, n) for(i = 0;i < n; ++i)
#define FI(i, st, ft) for(i = st;i <= ft; ++i)
#define pb(a, b) a.push_back(b)
#define M 1000000

using namespace std;

li 
gcd ( li a, li b )
{
  if ( a==0 ) return b;
  return gcd ( b%a, a );
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	li t, cnt = 0, i, cur;
	cin >> t;
	while(t--){
		cout << "Case #" << ++cnt << ": ";
		cur = 0;
		li ans = 0;
		string s;
		li a, b;
		cin >> s;
		F(i, s.size()) if(s[i] == '/') s[i] = ' ';
		istringstream ss(s);
		ss >> a;
		ss >> b;
		li temp = gcd(a, b);
		a = a / temp;
		b = b / temp;
		FI(i, 0, 42){
			if( (1 << i) == b) break;
		}
		if(i == 43){ cout  << "impossible\n"; continue;} 
		while(1){
			++cur;
			if(a > b || b % 2 != 0) { ans = 100; break; }
			if(a * 2 - b >= 0) { ans = cur; break; }
			b = b / 2;
		}
		if(ans <= 40) cout << ans << "\n";
		else cout  << "impossible\n" ;
	}
	return 0;
}
