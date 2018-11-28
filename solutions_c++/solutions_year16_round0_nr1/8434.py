/* Paras Narang 
 *
 */
#include <iostream>
#include <cstdio>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <cstring>
#include <map>
#include <cstdlib>
#include <algorithm>
#include <list>
#include <deque>
#include <bitset>
#include <cmath>
#include <set>
#include <sstream>

using namespace std;

#define oo 0x7F7F7F7F
#define LET(x,a)     __typeof(a) x(a)
#define EACH(it,v)   for(LET(it,v.begin());it!=v.end();++it)
#define REP(i,n)     for(__typeof(n) i(0); i<n; i++)
#define FOR(i,j,n)   for(__typeof(n) i(j); i<n; i++)
#define ALL(x)       (x).begin(), (x).end()
#define gint(t)      scanf("%d", &t);
#define pint(t)      printf("%d\n", t);
#define pb           push_back
#define mp           make_pair

typedef long long int   ll;
typedef unsigned long long int ull;
typedef unsigned int    uint;
typedef pair<int, int>  pii;
typedef vector<int>     vi;
typedef vector<vi>      vii;
typedef vector<pii>     vpii;

string processDigits(ll n, string numbers){
    do {
	int digit = n % 10;
	numbers[digit] = '1';
	n /= 10;
    } while (n > 0);
    return numbers;
}

int main() {
    int t; gint(t);
    REP(ti, t) {
	string numbers = "0000000000";    
        ll input;
	cin >> input;
	if (input == 0){
	    cout << "Case #" << ti+1 << ": INSOMNIA" << endl;
	    continue;
	}
	ll res = input;
	numbers = processDigits(res, numbers);

	while(numbers != "1111111111"){
	    res += input;
	    numbers = processDigits(res,numbers);
	}
	cout << "Case #" << ti+1 << ": " << res << endl;
    }
    return 0;
}

