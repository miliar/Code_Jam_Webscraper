///SACAR FREOPEN.
#include <iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<set>
#include<list>
#include<cstdlib>
#include<cstdio>
#include<iomanip>
#include<stack>
#include<queue>
#include<stdio.h>
#include<string.h>
#include<map>
#include<sstream>
#include<assert.h>

using namespace std;

#define all(c) (c).begin(),(c).end()
#define forn(i,n) for(int i=0; i<(int)n; i++)
#define dforn(i,n) for(int i=(int)n-1; i>=0; i--)
#define formn(i,m,n) for(int i=m; i<(int)n; i++)
#define dformn(i,m,n) for(int i=n-1; i>=m; i--)
#define mp make_pair
#define pb push_back

const double PI=acos(-1.0);

typedef long long tint;
typedef pair<int,int> pint;

typedef pair<int, char> Quat;

Quat simple_mul(char x, char y){
	if(x == 'e')
		return mp(1,y);
	if(y == 'e')
		return mp(1,x);
	if(x == y)
		return mp(-1,'e');
	if(x == 'i' && y == 'j')
		return mp(1,'k');
	if(x == 'i' && y == 'k')
		return mp(-1,'j');
	if(x == 'j' && y == 'i')
		return mp(-1,'k');
	if(x == 'j' && y == 'k')
		return mp(1,'i');
	if(x == 'k' && y == 'i')
		return mp(1,'j');
	if(x == 'k' && y == 'j')
		return mp(-1,'i');
	assert(false);
}

Quat mul(Quat q1, Quat q2){
	int s1 = q1.first;
	char l1 = q1.second;
	int s2 = q2.first;
	char l2 = q2.second;
	
	Quat q = simple_mul(l1, l2);
	int s3 = s1 * s2 * q.first;
	char q3 = q.second;
	return mp(s3, q3);
}

Quat prod(string & t){
	Quat res = mp(1,'e');
	forn(i, t.size())
		res = mul(res, mp(1,t[i]));
	return res;
}

int get(string & t, Quat q){
	Quat p = mp(1,'e');
	forn(i, t.size()){
		p = mul(p, mp(1,t[i]));
		if(p == q)
			return i + 1;
	}
	return 100000000;
}

int main(){
freopen("C.in","r",stdin);
freopen("C.out","w",stdout);
	int TC;
	cin >> TC;
	
	forn(tc,TC){
		int len;
		int times;
		string s;
		cin >> len >> times >> s;
		
		string t = "";
		forn(asdf, times)
			t += s;
		
		bool ok = false;
		
		if(prod(t) == mp(-1,'e')){
			int l1 = get(t,mp(1,'i'));
			if(l1 != 100000000){
				string t1 = t.substr(0,l1);
				assert(prod(t1) == mp(1,'i'));
				string t23 = t.substr(l1,t.size() - l1);
				assert(mul(prod(t1), prod(t23)) == mp(-1,'e'));
				int l2 = get(t23, mp(1,'j'));
				if(l2 != 100000000){
					string t2 = t23.substr(0,l2);
					assert(prod(t2) == mp(1,'j'));
					int l3 = (int)t.size() - l1 - l2;
					string t3 = t23.substr(l2, t23.size() - l2);
					assert(prod(t3) == mp(1,'k'));
					ok = true;
				}
			}
		}
		
		string res = "NO";
		if(ok)
			res = "YES";
		
		cout << "Case #" << tc + 1 << ": " << res << endl;
	}
    return 0;
}
