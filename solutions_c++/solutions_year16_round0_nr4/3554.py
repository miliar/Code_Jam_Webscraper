#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
#include <iomanip>

using namespace std;

#define LL long long

#define FOR(i,a,b) for(int i = a ; i < b ; i++)

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin >> T;
	FOR(tc,1,T+1)
	{
		int k,c,s;
		cin >> k >> c >> s;
		cout << "Case #" << tc << ": ";
		FOR(i,1,s+1)
		{
			cout << i << " ";
		}
		cout << endl;
	}
	return 0;
}
