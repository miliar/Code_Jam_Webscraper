#include <cstdio>
#include <cstdlib>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define debug(v) cerr << #v << ": " << (v) << endl

int solve(const vector<double>& a, const vector<double>& b){
    int ans = 0, ai = 0, bi = 0;
    while(ai < a.size() && bi < b.size()){
        if(a[ai] > b[bi]){
            ai ++; bi ++;
            ans ++;
        }
        else{
            bi ++;
        }
    }
    return ans;
}

int main(){
    int T;
    scanf("%d", &T);
    for(int t = 0; t < T; ++t){
        int N;
        scanf("%d", &N);
        vector<double> a(N), b(N);
        for(int i = 0; i < N; ++i)
            scanf("%lf", &a[i]);
        for(int i = 0; i < N; ++i)
            scanf("%lf", &b[i]);
        sort(a.begin(), a.end());
        reverse(a.begin(), a.end());
        sort(b.begin(), b.end());
        reverse(b.begin(), b.end());
        printf("Case #%d: %d %d\n", t + 1, solve(a,b), N - solve(b,a));
    }
    return 0;
}

