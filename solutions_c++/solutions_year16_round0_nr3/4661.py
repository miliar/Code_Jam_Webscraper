/**
* Change is impossible in this fog of ignorance.
*/
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <climits>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <cassert>
#include <cmath>
using namespace std;

#define trace(x) {cerr << #x << "=" << x <<endl;}
#define trace2(x, y) {cerr << #x << "=" << x << " " << #y << "=" << y <<endl;}
#define track(x) {cerr << #x << ":" << endl; for (int q = 0; q < x.size(); q++) {cerr << x[q] << " ";} cerr << endl;}
#define trackarr(x, n) {cerr << #x << ":" << endl; for (int q = 0; q < n; q++) {cerr << x[q] << " ";} cerr << endl;}
#define trackvv(x) {cerr << #x << ":" << endl; for (int i = 0; i < x.size(); i++) { cerr << "i:" << i << endl; for (int j = 0; j < x[i].size(); j++){cerr << x[i][j] << " ";} cerr << endl;} cerr << endl;}
#define trackcr(x) {cerr << #x << ":" << endl; for (auto i = x.begin(); i != x.end(); i++) {cerr << *i << " ";} cerr << endl;}
template <typename Tk, typename Tv> ostream& operator<<(ostream& os, const pair<Tk, Tv> &p){os << "{" << p.first << ',' << p.second << "}";return os;}

typedef long long ll;
typedef pair<int,int> ii;

const int MAX = 100005;
const int MOD = 1000000000+7;
const int INF = 1000000000;

long long mul(long long a,long long b,long long MOD){
	long long a_high=	a/1000000000;
	long long a_low =	a%1000000000;

	long long b_high=	b/1000000000;
	long long b_low =	b%1000000000;

	long long result = (a_high*b_high)%MOD;
	for(int i=0;i<9;i++)
		result=(result*10)%MOD;
	result=(result+a_high*b_low+a_low*b_high)%MOD;
	for(int i=0;i<9;i++)
		result=(result*10)%MOD;
	result=(result+a_low*b_low)%MOD;
	return result;
}

long long p(long long a,long long b,long long MOD){
	if(b==0) return 1;
    long long x=p(a,b/2,MOD);
    if((b&1)==0) {
	   return mul(x,x,MOD);
    } else {
	   return mul(mul(x,x,MOD),a,MOD);
    }
}

bool fermat(long long num,int iterations){
	if(num==1) {
		return false;
    } else if(num==2) {
		return true;
    } else {
		for(int i=0;i<iterations;i++){
			long long a=(rand()%(num-2))+2;
			if(p(a,num-1,num)!=1) return false;
		}
	}
	return true;
}

template <typename T>
string toString(T x){
    string s;
    while (x) {
        s.push_back(x % 2 + '0');
        x /= 2;
    }
    reverse(s.begin(), s.end());
    return s;
}

long long toValue(string &x, int base){
    long long sum = 0;
    for (int i = 0; i < x.size(); i++) {
        sum *= base;
        sum += (x[i]-'0');
    }
    return sum;
}

int main() {
    freopen("C-small.out", "w", stdout);

    int tc;
    cin >> tc;
    for (int t = 1; t <= tc; t++){
        printf("Case #%d: \n", t);
        int n, k;
        cin >> n >> k;
        for (int i = 1; i <= 1000000; i++) {
            string x = toString(i);
            int size = x.size();
            if ((size == n) && (x[size-1] == '1')) {
                bool flag = true;
                for (int j = 2; j <= 10; j++) {
                    ll value = toValue(x, j);
                    if (fermat(value, 50)) {
                        flag = false;
                    }
                }
                if (flag) {
                    cout << x << " ";
                    k--;
                    for (int j = 2; j <= 10; j++) {
                        ll value = toValue(x, j);
                        for (int j = 2; j < value; j++) {
                            if (value % j == 0) {
                                cout << j << " ";
                                break;
                            }
                        }
                    }
                    cout << endl;
                    if (k == 0) break;
                }
            }
        }
    }
}
