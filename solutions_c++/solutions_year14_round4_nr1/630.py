#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cstring>
#include <cstdlib>

#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <algorithm>
#include <utility>
#include <stack>
#include <queue>
#include <complex>
#include <iomanip>
using namespace std;

#define pb push_back
#define mp make_pair

typedef long long ll;
typedef vector<vector<int> > graph;
const int INF = 1000000000;
const ll MOD = 1000000009;
#define FILEIN "A.in"
#define FILEOUT "A.out"


int cnt[705];
int main(){
    freopen(FILEIN, "r", stdin);
    freopen(FILEOUT, "w", stdout);
    int tests;
    cin >> tests;
    for (int _ = 1; _ <= tests; ++_){
        memset(cnt, 0, sizeof cnt);
        int N;
        cin>>N;
        int cap;
        cin>>cap;
        for(int i = 0; i < N; ++i){
            int tmp;
            cin>>tmp;
            cnt[tmp]++;
        }
        int res = 0;
        for(int i = cap; i > cap/2; --i){
            for(int j = cap - i; j >= 0; --j){
                int take = min(cnt[j], cnt[i]);
                res += take;
                cnt[i] -= take;
                cnt[j] -= take;
            }
            res += cnt[i];
        }
        int sum = 0;
        for(int i = 0; i <= cap/2; ++i){
            sum += cnt[i];
        }
        res += (sum + 1)/2;
        cout << "Case #" << _ << ": ";
        cout<<res<<endl;
    }
    return 0;
}