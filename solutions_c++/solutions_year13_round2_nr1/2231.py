#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <sstream>
#include <fstream>
#include <limits>
#include <eigen3/Eigen/Dense>

using namespace std;

#define LL long long
#define LD long double
#define PR pair<int,int>

#define For(i,m,n) for (int i=m; i<int(n); i++)
#define ForR(i,m,n) for (int i=int(n)-1; i>=m; i--)

#define Sz(s) int((s).size())
#define All(s) (s).begin(),(s).end()
#define Fill(s,v) memset(s,v,sizeof(s))

template<typename T> T abs(T x) { return(x < 0 ? -x : x); }
template<typename T> T sqr(T x) { return(x*x); }

const LL INF = numeric_limits<LL>::max();
const LD EPS = 1e-9;
const LD PI = acos(-1.0);

#define DEBUG 0
#define LIM 1000

ifstream input;
ofstream output;
int numTest;
int test;
int A, N;

int search(int y, const vector<int> &x, int n){
	cout << n <<endl;
	if(n == N-1)
		return y>x[n] ? 0 : 1;
	if(y>x[n])
		return search(y+x[n], x, n+1);
	return 1+min(search(2*y-1, x, n), search(y,x,n+1));
}

int main(int argc, char**argv)
{
    clock_t start = clock();
    input.open(argc>1 ? argv[1]: "a2.in");
    //input.open(argc>1 ? argv[1]: "~/Downloads/A-small-attempt0.in");
    //input.open(argc>1 ? argv[1]: "~/Downloads/A-large.in");
    output.open(argc>2 ? argv[2]: "a.out");

    input >> numTest;
    For(test,1,numTest+1){
    	output << "Case #" << test <<": ";
    	input >> A >> N;
    	vector<int> x(N);
    	For(i,0,N){
    		input >> x[i];
    	}
    	sort(All(x));
    	int result = A == 1 ? N : search(A,x,0);

    	output << result <<endl;
    }

    cout << "Time: " << (clock()-(double)start)/(double)CLOCKS_PER_SEC << endl;

    return 0;

}
