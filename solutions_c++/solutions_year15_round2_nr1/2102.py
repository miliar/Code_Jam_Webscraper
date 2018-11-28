#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <math.h>
#include <iomanip>
#include <algorithm>
#define MAX_N 1000000
using namespace std;

void read();
long long solve(long long n);
long long flip_num(long long x);
void write(int caseNum, long long ans);

int ans[MAX_N+1];


int main(){
    read();
    return 0;
}

long long flip_num(long long x){
    long long y = x, ans = 0;
    if(x <= 10 || x%10 == 0) return x;
    for(int i = 0; i <= log10(x); i++){
        ans *= 10;
        ans += y%10;
        y /= 10;
    }
    return ans;
}

long long solve(long long n){
    long long flip, x;
    for(int i = 1; i <= 20; i++){
        ans[i] = i;
    }
    for(int i = 21; i <= n; i++){
        flip = flip_num(i);
        if(flip < i){
            ans[i] = min(ans[i-1]+1, ans[flip]+1);
        }else{
            ans[i] = ans[i-1]+1;
        }
    }
    return ans[n];
}

void read(){
    freopen("A-small-attempt2.in","r",stdin);
    freopen("results.txt","w",stdout);
    long long T, N;
    cin >> T;
    for(int t = 0; t < T; t++){
        cin >> N;
        write(t, solve(N));
    }
    return ;
}

void write(int caseNum, long long ans){
    cout << "Case #" << caseNum+1 << ": " << ans << endl;
    return ;
}
