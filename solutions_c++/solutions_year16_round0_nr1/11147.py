#include <math.h>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <bitset>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#include <ctime>
#include <assert.h>
#include <fstream>
#include <fstream>
#include <memory>
#include <functional>
#include <iterator>
#include <limits>
#include <stdexcept>
using namespace std;

typedef long long ll;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif

#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define forn (i,k,n) for (int i=k;i<n;i++)
//#define fornn(i,k,n) for(int i=k;i<=n;i++)
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T; cin >> T;
	
	int cnt = 1;
	while (cnt <= T) {

		long long int N;
		cin >> N;
		if (N == 0)
			cout << "Case #" << cnt << ": " << "INSOMNIA\n";
		else {

			int mask = 0;
			long long n = N;
			for (;;) {

				long long int k = n;
				while (k > 0){
					int i = k % 10;
					mask |= (1 << i);
					k /= 10;
				}
				if (mask == 1023)
				{
					cout <<"Case #"<<cnt<<": "<<n << endl;
					break;
				}
				n += N;

			}
		}

		cnt++;
	}


}


