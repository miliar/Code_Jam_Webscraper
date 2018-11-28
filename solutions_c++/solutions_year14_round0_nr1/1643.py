#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <set>
#include <stack>
#include <queue>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)
#define REPD(i, n) for (int i((n) - 1); i >= 0; --i)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

template<typename T> int size(const T& c) { return int(c.size()); }
template<typename T> T abs(T x) { return x < 0 ? -x : x; }
template<typename T> T sqr(T x) { return x*x; }
template<typename T> bool remin(T& x, T y) { if (x <= y) return false; x = y; return true; }
template<typename T> bool remax(T& x, T y) { if (x >= y) return false; x = y; return true; }
template<typename T> inline string itos(T n) {return (n)<0?"-"+itos(-(n)):(n)<10?(string)("")+(char)('0'+(n)):itos((n)/10)+itos((n)%10);}

ifstream fin("input");
ofstream fout("output");

string doCase(){
	int n,temp;
	int list1[4];
	int list2[4];

	fin>>n;
	REP(i,(n-1)*4) fin>>temp;
	REP(i,4) fin>>list1[i];
	REP(i,(4-n)*4) fin>>temp;

	fin>>n;
	REP(i,(n-1)*4) fin>>temp;
	REP(i,4) fin>>list2[i];
	REP(i,(4-n)*4) fin>>temp;

	int result=0;
	REP(i,4){
		REP(j,4){
			if(list1[i]==list2[j]){
				if(result==0)
					result=list1[i];
				else
					result=-1;
			}
		}
	}
	if(result==0) return "Volunteer cheated!";
	if(result==-1) return "Bad magician!";
	return itos(result);
}

int main(){
    int nn;
    fin>>nn;
    REP(ii,nn){
    	fout<<"Case #"<<ii+1<<": "<<doCase()<<endl;
    	//double: <<fixed<<setprecision(10)
    }
    return 0;
}
