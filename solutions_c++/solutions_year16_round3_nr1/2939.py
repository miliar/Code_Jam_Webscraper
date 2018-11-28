#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
#include <deque>
#include <unordered_map>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)
const int MOD = 1000002013;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
int bc(int n) { return n ? bc((n-1)&n)+1 : 0; }

int T, N;

int flag = 1;
	std::map<char, int> l;
int main() {
	freopen("A-small-attempt0.in", "r", stdin);

	int *x;
	int max, umax;
	int y, acc;
	//freopen("A-small-practice.in", "r", stdin);
	//freopen("A-small-practice.out", "w", stdout);

	//freopen("A-large-practice.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	cin >> T;

	F1(i,T) {
		
		cin >> N;
		x = new int(N);
		acc =0;
		F0(j,N) {
		
			cin >> x[j];
			acc += x[j];
					
		}
		
		//cerr << N << K;
		cout << "Case #" << i << ":";
		
		flag = 1;
		
		while (1)
		{
			max  = 0;
			F0(k, N) {
				if (x[max] < x[k])
					max = k;
					//cerr << " " << max << " ";
			}
			x[max]--;
			umax = 0;
			F0(k, N) {
				if (x[umax] < x[k])
					umax = k;
			}		
			x[umax]--;	
			
			if (acc % 2 == 0) {
				cout << " " << (char)('A'+max)<< (char)('A'+umax);
				acc -= 2;
			}
			else {
				cout << " " << (char)('A'+max);
				x[umax]++;	
				acc -= 1;
			}
			
			if (acc == 0)
				break;
			 
		}
		cout << endl;
		//cin >> y;
		delete(x);
	}

	return 0;
}






