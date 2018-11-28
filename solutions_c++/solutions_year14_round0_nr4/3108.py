#include <cstdio>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <cstring>
#include <cctype>
#include <queue>

using namespace std;

typedef long long          ll;
typedef pair <int, int>    ii;
typedef vector <ii>       vii;
typedef vector <int>       vi;
#define INF 1000000000
#define pb push_back
#define mp make_pair


vector<long double> N1, K1;
vector<long double> N, K;

int main() {
    freopen ("inputC.txt","r",stdin);
    freopen ("outputC.txt","w",stdout);
    int k;
    scanf(" %d", &k);
    for (int a = 1; a <= k; a++) {
        int n;
        N.clear(); K.clear();
        scanf(" %d", &n);

        for (int i = 0; i < n; i++) {
            long double temp;
            scanf(" %Lf", &temp);
            N.pb(temp);
            N1.pb(temp);
        }
            for (int i = 0; i < n; i++) {
            long double temp;
            scanf(" %Lf", &temp);
            K.pb(temp);
            K1.pb(temp);
        }

        sort(N.begin(), N.end());
        sort(K.begin(), K.end());
        sort(N1.begin(), N1.end());
        sort(K1.begin(), K1.end());

        int normal = 0;
        int N1size = N1.size();
        while (N1size != 0) {
            long double escolhido = N1[0];
            if (K1[N1size-1] > escolhido) {
                for (int i = 0; i < N1size; i++) {
                    if (K1[i] > escolhido) {
                        K1.erase(K1.begin()+i);
                        N1.erase(N1.begin());
                        break;
                    }
                }
            } else {
                normal++;
                K1.erase(K1.begin());
                N1.erase(N1.begin());
            }
            N1size--;
        }


        int outro = 0;
        int Nsize = N.size();
        while (Nsize != 0) {
            if (N[Nsize-1] > K[Nsize-1]) {
                outro++;
                N.pop_back();
                K.pop_back();
            } else {
                N.erase(N.begin());
                K.pop_back();
            }
            Nsize--;
        }
        printf("Case #%d: %d %d\n", a, outro, normal);
    }
    return 0;
}
