#include <queue>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
#include <fstream>
#include <cstring>
#include <string>
#include <climits>
#include <random>
using namespace std;

//macros
typedef long long ll;
typedef complex<double> point;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector< vector<int> > vvi;




#define FOR(k,a,b) for(int k=(a); k<=(b); ++k)
#define REP(k,a) for(int k=0; k<(a);++k)
#define SZ(a) int((a).size())
#define ALL(c) (c).begin(),(c).end()
#define PB push_back
#define MP make_pair
#define INF 999999999
#define INFLONG 1000000000000000000
#define MOD 1000000007
#define MAX 100
#define ITERS 100
#define MAXM 200000
#define MAXN 100000
#define _gcd __gcd
#define eps 1e-9
#define pi 3.1415926535897932384626

int main()
{
    int test;
    ifstream fin("dat.dat");
    ofstream fout("dat.out");
    fin >> test;
    for(int tes = 1; tes <= test; tes++){
        string str;
        fin >> str;
        string ret = "";
        ret += str[0];
        char ch = str[0];
        for(int i = 1; i < str.length(); i++){
            string stra = str[i] + ret;
            string strb = ret + str[i];
            if(stra<=strb){
                ret = strb;
            }
            else{
                ret = stra;
            }
        }
        fout << "Case #" << tes << ": " << ret << endl;
       // cout << "Case #" << tes << ": " << ret << endl;
    }
    fout.close();
}
