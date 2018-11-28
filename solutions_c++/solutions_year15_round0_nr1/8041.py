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
#include <memory.h>
#include <ext/hash_map>
using namespace std;
using namespace __gnu_cxx;

#define SZ(X) (int)(X).size()
#define ALL(X) (X).begin(),(X).end()
#define ALLR(X) (X).rbegin(),(X).rend()

const double EPS = 1e-9;
const int INF = 1<<28;
const long long INFL = 1LL<<62;

using namespace std;

int main() {

    int t;
    cin >> t;
    int max_s;
    string x;
    int w=1;

    while(t){

        cin >> max_s;
        cin >> x;
        int m=0,c=0;
        for(int i=0;i<max_s;i++){

        	c+=x[i]-'0';
        	if(c<i+1){
        		m++;
        		c++;
        	}
        }


        cout << "Case #"<< w <<": " << m<<endl;
        w++;
        t--;
    }

	return 0;
}
