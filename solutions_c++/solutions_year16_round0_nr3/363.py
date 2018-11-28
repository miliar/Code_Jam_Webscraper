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

int n, m;

long long getnumber(int mask, int base) {

    long long num = 1;

    for (int i=n-3; i>=0; i--) {

        num = (num*base) + ((mask&(1<<i)) > 0);

    }

    num = (num*base) + 1;

    return num;
}

bool isprime(long long x) {

    for (long long i=2; i*i<=x; i++) {
        if (x%i==0) return false;
    }

    return true;

}

long long getdiv(long long x) {

    for (long long i=2; i*i<=x; i++) {
        if (x%i==0) return i;
    }

    return -1;

}

string getbinary(int mask) {

    char buf[n+1];
    buf[0] = '1';
    for (int i=n-3; i>=0; i--) {
        buf[n-i-2] = ((mask&(1<<i)) > 0 ? '1': '0');
    }
    buf[n-1] = '1';
    buf[n] = 0;
    return (string)buf;
}

int main() {

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int ncases;
    cin>>ncases;
    for (int cas=1; cas<=ncases; cas++) {

        cin>>n>>m;
        long long num = 0;
        vector<int> ans;

        for (int i=0; i<(1<<(n-2)) && ans.size() < m; i++) {

            //cout<<i<<" "<<ans.size()<<endl;

            bool found = false;
            for (int j=2; j<=10 && !found; j++) {
                num = getnumber(i, j);
                //cout<<num<<endl;
                if (isprime(num)) {
                    found = true;
                }
            }

            if (!found) {
                ans.push_back(i);
            }
        }

        printf("Case #%d:\n", cas);
        for (int i=0; i<ans.size(); i++) {
            cout<<getbinary(ans[i])<<" ";
            for (int j=2; j<=10; j++) {
                num = getnumber(ans[i], j);
                cout<<getdiv(num)<<" ";
            }
            cout<<endl;
        }

    }

    return 0;

}
