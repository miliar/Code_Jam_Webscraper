/*
ID: nenad.11
PROG: maze1
LANG: C++11
*/
#include <iostream>
#include <string>
#include <stack>
#include <vector>
#include <queue>
#include <deque>
#include <algorithm>
#include <set>
#include <ctime>
#include <utility>
#include <functional>
#include <map>
#include <sstream>
#include <cmath>
#include <fstream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <cstdio>

using namespace std;

#define endl "\n"
#define inf 1000000010
#define llinf 9000000000000000000
#define trace(x) cout << (x) << endl;
#define trace2(x,y) cout << (x) << " " << (y) << endl;
#define trace3(x,y,z) cout << (x) << " " << (y) << " " << (z) <<  endl;
#define trace4(x,y,z,q) cout << (x) << " " << (y) << " " << (z) << " " << (q) <<  endl;
#define trace5(x,y,z,q,w) cout << (x) << " " << (y) << " " << (z) << " " << (q) << " " << (w) <<  endl;
#define trace6(x,y,z,q,w,e) cout << (x) << " " << (y) << " " << (z) << " " << (q) << " " << (w) << " " << (e) <<  endl;
#define min3(x,y,z) min( (x), min( (y), (z)  )   )
#define max3(x,y,z) max( (x), max( (y), (z)  )   )
#define max4(x,y,z,q) max( max( (x), (q) ), max( (y), (z)  )   )
#define all(x) (x).begin(),(x).end()
#define pb push_back
#define mp make_pair
#define mpp(one,two,three) make_pair( one,  make_pair( two, three ) )
#define tp(one) cout << (one).first << " " << (one).second << endl;
#define tpp(one) cout << (one).first << " " << (one).second.first << " " << (one).second.second << endl;
#define ms(thing, val) memset( (thing), (val), sizeof(thing) )
#define mt make_tuple
#define fori(lim) for(int (i) = (0); (i) < (lim);(i)++ )
#define forj(lim) for(int (j) = (0); (j) < (lim);(j)++ )
#define fork(lim) for(int (k) = (0); (k) < (lim);(k)++ )
typedef pair<int, int> pii;
typedef pair<int, pair<int, int> > piii;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef long long ll;

int n, m, t, t1, t2, t3, t4, f, k;
/*
void pvi(vector<int>& thinger){ for (int q = 0; q < thinger.size(); q++) cout << thinger[q] << ", "; cout << endl; }
void pvc(vector<char>& thinger){ for (int q = 0; q < thinger.size(); q++) cout << thinger[q] << ", "; cout << endl; }
void pvs(vector<string>& thinger){ for (int (q) = 0; (q) < thinger.size(); (q)++) cout << (thinger[(q)]) << ", "; cout << endl; }
void pvb(vector<bool>& thinger){ for (int q = 0; q < thinger.size(); q++) cout << thinger[q] << ", "; cout << endl; }
void pvvi(vector<vector<int> >& t){ for (auto q : t)  pvi(q); }
void pvll(vector<ll>& thinger){ for (int q = 0; q < thinger.size(); q++) cout << thinger[q] << ", "; cout << endl; }
void pvpii(vector<pii>& thinger){ for (auto q : thinger) cout << q.first << " " << q.second << ", "; cout << endl; }
void pvvll(vector<vector<ll> >& t){ for (auto q : t)  pvll(q); }
int gcf(int a, int b)
{
	if (b > a) return gcf(b,a);
	if (b == 0) return a;
	return gcf(b, a%b);
}
int lcm(int a, int b){ return (a*b) / gcf(a, b); }
//MAKE INPUT WAY FASTER, BUT ONLY IF YOURE USING C++ I/O ONLY --> ios::sync_with_stdio(false);
bool isprime(int k)
{
	if (k <= 1) return 0;
	if (k == 2) return 1;
	if (k % 2 == 0) return 0;
	for (int i = 3; i*i <= k; i += 2)
		if (k % i == 0) return 0;

	return 1;
}
const long long llmod = 1000000000000000007LL;
//const long long llmod = 101LL;
const int mod = 1000000007;
//#define getchar getchar_unlocked
//#define putchar putchar_unlocked*/
int fi(){ int ip = getchar(), ret = 0, flag = 1; for (; ip<'0' || ip>'9'; ip = getchar())if (ip == '-'){ flag = -1; ip = getchar(); break; }for (; ip >= '0'&&ip <= '9'; ip = getchar())ret = ret * 10 + ip - '0'; return flag*ret; }
void fo(int n)     { if (n<0){ n = -n; putchar('-'); }int i = 10; char output_buffer[11]; output_buffer[10] = '\n'; do{ output_buffer[--i] = (n % 10) + '0'; n /= 10; } while (n); do{ putchar(output_buffer[i]); } while (++i<11); }
#define read_speed ios::sync_with_stdio(0);cin.tie(0)
//MAKE INPUT WAY FASTER, BUT ONLY IF YOURE USING C++ I/O ONLY --> ios::sync_with_stdio(false);
//TIME clock_t start = clock(); cout << "Time: " << (clock() - start) / (double)(CLOCKS_PER_SEC / 1000) << " ms" << endl;
#define x first
#define y second

#define llj(var , start , lim) for(int (var) = (start); (var) < (lim); (var)++)

/*------------------------------------------------THE END-----------------------------------------------------------*/


int main()
{
	read_speed;
	ifstream in("test.txt");
	freopen("ouptut.txt" , "w" , stdout);
	in >> f;
	string s;

	llj(z , 1  , f+1){
		in >> n >> s;

		int have = 0 , needed = 0;

		fori(n+1)
		{
			int cur = s[i] - '0';
			//trace4(cur ,i, have , needed)
			if (cur){
				if (have >= i){
					have += cur;
				}
				else{
					needed += i - have;
					have += i - have;
					have += cur;
				}

			}
		}
		printf("Case #%d: %d\n" , z , needed);
		//cout << endl;
	}


	return 0;
}