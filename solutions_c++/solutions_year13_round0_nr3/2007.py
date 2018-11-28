#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define FOR(i, a, b) for (long long i(a), _b(b); i <= _b; ++i)
#define REP(i, n) for (long long i(0), _n(n); i < _n; ++i)

long long unfair_squares[] = {	1, 
								4, 
								9, 
								121, 
								484, 
								10201, 
								12321, 
								14641, 
								40804, 
								44944, 
								1002001, 
								1234321, 
								4008004, 
								100020001, 
								102030201, 
								104060401, 
								121242121, 
								123454321, 
								125686521, 
								400080004, 
								404090404, 
								10000200001, 
								10221412201, 
								12102420121, 
								12345654321, 
								40000800004, 
								1000002000001, 
								1002003002001, 
								1004006004001, 
								1020304030201, 
								1022325232201, 
								1024348434201, 
								1210024200121, 
								1212225222121, 
								1214428244121, 
								1232346432321, 
								1234567654321, 
								4000008000004, 
								4004009004004};

int main(void){
	int ntest;
	ifstream fin("C-large-1.in");
	ofstream fout("out.txt");

	long long A,B;
	int ret;

	fin >> ntest;
	REP(w,ntest){
 		ret = 0;
		fin >> A >> B;
		REP(i,39){
			if((unfair_squares[i]>=A) && (unfair_squares[i]<=B))ret++;
		}
		fout << "Case #" << w+1 << ": " << ret << endl;
	}

	fin.close();
	fout.close();
	return 0;
}