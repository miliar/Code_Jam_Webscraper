#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

typedef long long LL;
#define rep(it,s) for(__typeof((s).begin()) it=(s).begin();it!=(s).end();it++)

#define DEBUG false

int main() {

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int ncases;
    cin>>ncases;

    for (int cas=1; cas<=ncases; cas++) {

        long long n;
        cin>>n;

        if (n==0) {
            printf("Case #%d: INSOMNIA\n", cas);
        }
        else {
            long long cur = n;
            set<int> digits;

            int iter = 0;

            while (digits.size() < 10) {

                long long x = cur;
                while (x>0) {
                    digits.insert(x%10);
                    x /= 10;
                }

                cur += n;

                iter++;

                if (iter > 1000) {
                    cerr<<"No se ha encontrado solucion en el caso N = "<<n<<endl;
                    break;
                }
            }

            if (DEBUG)
                cerr<<"Se ha conseguido la solucion: "<<(cur-n)<<" en "<<iter<<" iteraciones."<<endl;
            printf("Case #%d: %d\n", cas, cur-n);
        }

    }

    return 0;

}
