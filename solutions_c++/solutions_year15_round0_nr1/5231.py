#include <iostream>
#include <cstdlib>
#include <cstdio>
using namespace std;

int main(){
    int t;
    cin >> t;
    for (int tt = 0; tt < t; ++tt){
        int n, sum = 0, ret = 0;
        cin >> n;
        char x;
        for (int i = 0; i < n + 1; ++i){
            cin >> x;
            if (i > sum){
                ret += i - sum;
                sum += i - sum;
            }
            sum += x - '0';
        }
        printf("Case #%d: %d\n", (tt+1), ret);
    }
    return 0;
}
