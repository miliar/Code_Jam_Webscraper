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

int a[N], b[N];

int shiftleft(int left, int right){
    for(int i = right; i >= left + 1; i--){
        int tmp = b[i];
        b[i] = b[i-1];
        b[i-1] = tmp;
        //swap(&b[i], &b[i-1]);
    }
}
int shiftright(int right, int j){
    for(; j <= right - 1; j++){
        int tmp = b[j];
        b[j] = b[j + 1];
        b[j + 1] = tmp;
        //swap(&b[j], &b[j + 1]);
    }
}

int solve(){
    int n, i, j, ans = 0;
    cin>>n;
    int left = 1, right = n;
    for(i = 1; i <= n; i++){
        cin>>a[i];
        b[i] = a[i];
    }
    sort(a + 1, a + n + 1);
    for(i = 1; i <= n; i++){
        int x = a[i];
        for(j = 1; j <= n; j++){
            if(x == b[j]) break;
        }
        if(j - left <= right - j){
            shiftleft(left, j);
            ans += j - left;
            left ++;
        }
        else{
            shiftright(right, j);
            ans += right - j;
            right --;
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
