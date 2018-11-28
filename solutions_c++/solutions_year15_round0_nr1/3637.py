//Esteban Foronda Sierra
using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

template <class T> string toStr(const T &x)
{ stringstream s; s << x; return s.str(); }
template <class T> int toInt(const T &x)
{ stringstream s; s << x; int r; s >> r; return r;}

#define D(x) cout << #x " is " << x << endl

int main(){
	int n;
	cin >> n;
	int x = 1;
	while(n--){
		int p;
		cin >> p;
		string aud;
		cin >> aud;
		int ans = 0;
		int sum = aud[0] - '0';
		for(int i = 1; i < aud.size(); ++i){
			if (sum < i) {
				ans += (i - sum);
				sum = i + (aud[i] - '0');
			} else sum += aud[i] - '0';
		}
		printf("Case #%d: %d\n", x++, ans);
	}
	return 0;
}




