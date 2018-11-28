#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

const int MAXN = 2000;

int cmp1(double x , double y) {
    return x < y;
}

int cmp2(double x , double y) {
    return x > y;
}

int T , N , ret1 , ret2;
double a[MAXN] , b[MAXN];

int main () {
    freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);
    cin >> T;
    for (int i = 1;i <= T;i ++) {
        cin >> N;
        ret1 = ret2 = 0;
        for (int j = 0;j < N;j ++)
            cin >> a[j];
        for (int j = 0;j < N;j ++)
            cin >> b[j];
        sort(a,a+N,cmp1);
        sort(b,b+N,cmp2);
        int l = 0 , r = N-1;
        int j = 0;
        while (l <= r) {
              if (a[r] > b[j]) {
                 ret1 ++;
                 r --;
                 j ++;
              }
              else {
                 l ++;
                 j ++;
              }
        }
        sort(b,b+N,cmp1);
        sort(a,a+N,cmp2);
        l = 0;  r = N-1;
        j = 0;
        while (l <= r) {
              if (b[r] > a[j]) {
                 ret2 ++;
                 r --;
                 j ++;
              }
              else {
                 l ++;
                 j ++;
              }
        }
        cout << "Case #" << i << ": " << ret1 << " " << N - ret2 << endl;
    }
    return 0;
}
