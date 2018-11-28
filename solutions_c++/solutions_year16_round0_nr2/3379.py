#include <cstdio>
#include <math.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <functional>
#include <vector>
#include <queue>
#include <cstring>
#include <iomanip>
#include <deque>
#include <stack>
#include <map>
#include <set>

#define forn(i,n) for(int i=0;i<n;i++)

using namespace std;

typedef long long ll;

typedef unsigned long long ull;

typedef pair<int, int> P2;
typedef pair<ll, ll> P2l;

#define INF 1000000

string chk(string s1, int d){
	string t=s1;
	forn(i, d+1){
		if(t[i] == '+') s1[d-i] = '-';
		else s1[d-i] = '+';
	}
	return s1;
}


int main()
{
	int debug = 0;
	if(debug){
		freopen("test.txt", "w", stdout);
		srand((int)time(NULL));
		return 0;
	}
	
	freopen("B-large.in", "r", stdin);//test.txt//B-small-attempt0.in
	freopen("B-large.txt", "w", stdout);

	int T; cin>>T;
	forn(i,T) {
		string s; cin>>s;
		int ans=0;
		for(int j=s.size()-1; j>0; j--){
			if(s[j]=='-' && s[0]=='-') {ans++; s = chk(s, j); }
			else if (s[j]=='-' && s[0]=='+') {
				ans+=2;
				int m=0;
				forn(z, j) if(s[z]=='+') m=z;
				s = chk(s, m);
				s = chk(s, j); 
			}
		}

		if(s[0]=='-') ans++;
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}


	return 0;
}
