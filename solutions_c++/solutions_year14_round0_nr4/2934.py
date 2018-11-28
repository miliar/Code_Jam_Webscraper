#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define foreach(u, o) \
    for (typeof((o).begin()) u = (o).begin(); u != (o).end(); ++u)
const int INF = 2147483647;
const double EPS = 1e-9;
const double pi = acos(-1);
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
template <class T> T mod(T a, T b) { return (a % b + b) % b; }
template <class T> int size(const T &x) { return x.size(); }

int N;
vector<double> naomi(1000, 0.0);
vector<double> ken(1000, 0.0);

int war()
{
    int kenWin = 0;
    vector<double>::iterator kenit = ken.begin();
    vector<double>::iterator naomit = naomi.begin();
    while(kenit != ken.begin()+N){
        while(kenit != ken.begin()+N && *kenit < *naomit){
            kenit++;
        }
        if(kenit != ken.begin()+N){
            kenWin++;
            kenit++;
            naomit++;
        }
    }
    return N-kenWin;
}

int d_war()
{
    int naomiWin = 0;
    vector<double>::iterator kenit = ken.begin();
    vector<double>::iterator naomit = naomi.begin();
    while(naomit != naomi.begin()+N){
        while(naomit != naomi.begin()+N && *naomit < *kenit){
            naomit++;
        }
        if(naomit != naomi.begin()+N){
            naomiWin++;
            naomit++;
            kenit++;
        }
    }
    return naomiWin;
}

int main()
{
    int T;
    cin >> T;
    for(int t = 0; t < T; ++t){
        cin >> N;
        for(int i = 0; i < N; ++i){
            cin >> naomi[i];
        }
        for(int i = 0; i < N; ++i){
            cin >> ken[i];
        }
        sort(naomi.begin(), naomi.begin()+N);
        sort(ken.begin(), ken.begin()+N);
        printf("Case #%d: %d %d\n", t+1, d_war(), war());
    }
}
