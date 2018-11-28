#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <cassert>
#include <complex>

using namespace std;

#define ST first
#define ND second
#define MP make_pair
#define PB push_back

typedef long long LL;
typedef long double LD;

typedef vector<int> VI;
typedef pair<int,int> PII;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(VAR(i,a);i<=(b);++i)
#define FORD(i,a,b) for(VAR(i,a);i>=(b);--i)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)((a).size()))
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))
#define ZERO(x) memset(x,0,sizeof(x))

#define fabsl __builtin_fabsl
#define atan2l __builtin_atan2l
#define cosl __builtin_cosl
#define sinl __builtin_sinl
#define sqrtl __builtin_sqrtl


#define NUMBER 4

char table[NUMBER][NUMBER];
char result[100];
const int myvector[]={1, 4, 9, 121, 484};



const char * resultado[]={"NO","YES"};
int win=-1;
bool notfinis=false;
map<char,int> myset;
int ini,fin;

void alg() {
    int num=0;win=-1;notfinis=false;
	for (int i;i<5;i++)
		if(myvector[i]>=ini && myvector[i]<=fin)
			num++;
	cout<<num<<endl;
}




void leer(){

	cin>>ini>>fin;

}

int main() {
    int n_cases;
    cin >> n_cases;
    for (int test_case = 1; test_case <= n_cases; ++test_case) {
        cout << "Case #" << test_case << ": ";
        leer();
        alg();
    }
}
