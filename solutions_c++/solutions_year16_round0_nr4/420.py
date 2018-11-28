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

string s[10], str[10];

int K, c;
unsigned long long S;

unsigned long long fpow(unsigned long long a, int b) {
    if (b==0) return 1;
    unsigned long long tmp = fpow(a, b/2);
    tmp = tmp*tmp;
    if (b%2==0) return tmp;
    return a*tmp;
}

int main() {

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);


    int ncases;
    cin>>ncases;
    for (int cas=1; cas<=ncases; cas++) {

        cin>>K>>c>>S;

        unsigned long long m = fpow(K, c);

        int p = min(c, K);

        int needed = (K - 1) / p + 1;

        if (S < needed) {
            printf("Case #%d: IMPOSSIBLE\n", cas);
        }
        else if (c == 1) {
            if (S >= K) {
                printf("Case #%d: ", cas);

                for (int i=0; i<K; i++) {

                    cout<<i+1<<" ";

                }

                cout<<endl;
            }
            else {
                printf("Case #%d: IMPOSSIBLE\n", cas);
            }
        }
        else {

            printf("Case #%d: ", cas);

            for (int i=0; i<K; i+=p) {

                unsigned long long v = 0;

                i = min(i, K-p);

                //cout<<i<<endl;

                for (int j=0; j<min(c, K); j++) {
                    v += ((j+i))*fpow(K, c-j-1);
                    if (v < 0 || v > m) {
                        cerr<<v<<" "<<K<<" "<<c<<" "<<c-j<<" "<<i<<" "<<m<<endl;
                    }
                }

                cout<<v+1<<" ";

            }

            cout<<endl;

        }
    }


    /*
    K = 5;
    c = 3;

    unsigned long long m = fpow(K, c);

    string g;

    for (int k=0; k<K; k++) {
        for (int j=0; j<K; j++) s[k] += "L";
        s[k][k] = 'G';
        g += "G";
    }

    for (int k=0; k<K; k++) {
        str[k] = s[k];
        for (int i=0; i<c-1; i++) {

            string tmp = "";
            for (int j=0; j<str[k].length(); j++) {
                if (str[k][j]=='G') tmp += g;
                else tmp += s[k];
            }

            str[k] = tmp;

            cout<<str[k]<<endl;

        }
    }

    for (int j=0; j<str[0].length(); j++) {

        bool good = true;
        for (int k=0; k<K; k++) if (str[k][j]!='G') good = false;

        if (good) cout<<j<<" ";

    }

    cout<<endl;

    int v = 0;

    int t = 2;
    for (int j=0; j<c; j++) {

        v += (t+j)*(int)fpow(K, c-j-1);

    }
    cout<<v<<" "<<str[0].length()<<" "<<m<<endl;

    for (int k=0; k<K; k++) cout<<str[k][v]<<" ";
    */

    return 0;

}
