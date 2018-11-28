#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <valarray>
#include <vector>

#define pb push_back
#define pf push_front
#define sz size
#define f() first
#define s() second
#define b() begin()
#define e() end()

#define pairii pair< int,int >
#define vint vector< int >
#define vchar vector< char >
#define vbool vector< bool >
#define vstring vector< string >
#define int64 long long
#define Uint64 unsigned long long
#define Uint unsigned int
#define Uchar unsigned char

#define fori(n) for(int i=0;i<n;i++)
#define forj(n) for(int j=0;j<n;j++)
#define fork(n) for(int k=0;k<n;k++)
#define forir(n) for(int i=n-1;i>=0;i--)
#define forr(i, a, b) for ( int i = (a); i <= (b); ++i )
#define ford(i, a, b) for ( int i = (a); i >= (b); --i )
#define forit(v) for(it = v.begin();it != v.end();it++)

#define trace(x...) x
#define print(x...) trace(printf(x))
#define watch(x) trace(cout << #x" = " << x << "\n")

#define INF 0x3F3F3F3F // Signed int
//#define INF 0x3F3F3F3F3F3F3F3FLL // Signed int64
#define EPS 1e-10
#define PI 3.14159265358979323846

#define POSITIVE +1
#define NEGATIVE -1

#define MAP(a) ((a).l=='1'?0:((a).l=='i'?1:((a).l=='j'?2:3)))

int cmpD(double a, double b){
	return (a <= b + EPS) ? (a + EPS < b) ? -1 : 0 : 1;
}

using namespace std;

class letter{
	public: char l;	int sign;
	letter(char a, int b = POSITIVE) : l(a), sign(b) { }
	letter() {}
};

const letter table [4][4] = {
	{ letter('1'), letter('i'),           letter('j'),           letter('k') },
	{ letter('i'), letter('1', NEGATIVE), letter('k'),           letter('j', NEGATIVE) },
	{ letter('j'), letter('k', NEGATIVE), letter('1', NEGATIVE), letter('i') }, 
	{ letter('k'), letter('j'),           letter('i', NEGATIVE), letter('1', NEGATIVE) }
};

letter combine(letter a, letter b){
	int sign = POSITIVE;
	if( (a.sign == NEGATIVE && b.sign == POSITIVE) || (a.sign == POSITIVE && b.sign == NEGATIVE) )
		sign = NEGATIVE;
	letter ret = table[MAP(a)][MAP(b)];
	if( sign == NEGATIVE ){
		if( ret.sign == POSITIVE ) ret.sign = NEGATIVE;
		else if( ret.sign == NEGATIVE ) ret.sign = POSITIVE;
	}
	return ret;
}

int main(){

	int T, L, X;
	char buff[100000];
	vector<letter> in;


	scanf("%d", &T);

	fork(T){
		scanf("%d %d", &L, &X);
		in.resize(L*X);
		scanf("%s", buff);
		fori(X) forj(L) in[i*L+j] = letter(buff[j]);

		vint I;
		set<int> K;
		letter temp_i('1');
		letter temp_k('1');
		fori(L*X){
			temp_i = combine(temp_i, in[i]);
			if( temp_i.sign == POSITIVE && temp_i.l == 'i' )
				I.pb(i);
			temp_k = combine(in[L*X-1-i], temp_k);
			if( temp_k.sign == POSITIVE && temp_k.l == 'k' )
				K.insert(L*X-1-i);
		}

		bool ret = false;
		fori( I.sz() ){
			int init = I[i] + 1;
			letter temp('1');
			for(int j = init;j < L*X;j++){
				temp = combine(temp, in[j]);
				if( temp.sign == POSITIVE && temp.l == 'j' )
					if( K.find(j+1) != K.e() ){
						ret = true;
						break;
					}
			}
			if( ret ) break;
		}

		printf( "Case #%d: %s\n", k+1, ret ? "YES" : "NO" );



	}

	return 0;

}
