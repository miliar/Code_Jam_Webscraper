#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstdio>

using namespace std;

#define PB push_back
#define F first
#define S second
#define MP make_pair
#define N 100000

int a[N];
int solve(){
    int n, val, ans = 0, i, j;
    cin>>n>>val;
    for(i = 1; i <= n; i++){
        cin>>a[i];
    }
    sort(a + 1, a + n + 1);
    for(i = 1, j = n; i <= j; ){
        if(i == j){
            ans++;
            i++;
            continue;
        }
        if(a[i] + a[j] <= val){
            ans++;
            i++;
            j--;
            continue;
        }
        if(a[j] <= val){
            ans++;
            j--;
            continue;
        }

    }
    return ans;
}
int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int test = 1, o = 1;
    cin>>test;
    while(test--){
        printf("Case #%d: %d\n", o++, solve());

    }
    return 0;
}
