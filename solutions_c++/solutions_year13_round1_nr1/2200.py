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
#define pb push_back
#define mp make_pair
#define x first
#define y second

template<typename T> T Abs(T x) { return(x < 0 ? -x : x); }
template<typename T> T Sqr(T x) { return(x*x); }

const int INF = (int)1e9;
const LD EPS = 1e-9;
const LD PI = acos(-1.0);

#define DEBUG 0
#define LIM 1000

ifstream input;
ofstream output;
int numTest;
int test;

//////////////////////
int r;
int t;

int main(int argc, char**argv)
{
    clock_t start = clock();
    input.open(argc>1 ? argv[1]: "in.txt");
    output.open(argc>2 ? argv[2]: "out.txt");    

    input >> numTest;
//    numTest = 1;
    For(test,1,numTest+1){
	input >> r;
	input >> t;

	long long int min = 1;
	long long int max = 1000000000;
	int calcualted = 1;
	long long int average;
	cout << r <<" " <<t <<endl;
	double area;
	For(i,0,10000){
	    average = (long long int)((max+min)/2);
	    if(min>max){
		cout << average << " " <<area <<endl;
		break;
	    }
	    area = 2*average*(r+0.5)+2*(average-1)*(average);

	    if(area>t){
		max = average-1;
	    }
	    else if(area<=t){
		min = average+1;
	    }
	}
	cout << "Case #" << test <<": " <<average <<endl;
	output << "Case #" << test <<": " <<average <<endl;
    }

    cout << "Time: " << (clock()-(double)start)/(double)CLOCKS_PER_SEC << endl;
    
    return 0;

}
