#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <iostream>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <iomanip>

#define rep(i,m) for(unsigned long long i = 0;i < (unsigned long long)m ;i++)
#define rep2(i,n,m) for(unsigned long long i = (unsigned long long)n;i < (unsigned long long)m ;i++)
#define ui unsigned int
#define ull  unsigned long long
#define pb  push_back

using namespace std;

int main() {
	vector<int> dat;
	dat.pb(1);
	dat.pb(4);
	dat.pb(9);
	dat.pb(121);
	dat.pb(484);
	int cases, A, B, out; 
	cin >> cases;
	rep(casei, cases){
		cin>>A>>B;
		out = 0;
		rep(i, dat.size())
			if(A <= dat[i] && B>= dat[i])
				out ++;
    	cout << "Case #"<< (int)casei + 1 <<": "<<out<< endl;
    }
    return 0;
}