#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

vector <double> va, vb;
double a[1005], b[1005];
int ans1, ans2, temp;

void run()
{
    int t, cnt=1;
    int n;
    scanf("%d", &t);
    while(t--) {
        ans1 = 0, ans2 = 0;
        scanf("%d", &n);
        for(int i = 0; i < n; i++) scanf("%lf", a + i);
        for(int i = 0; i < n; i++) scanf("%lf", b + i);
        sort(a, a + n);
        sort(b, b + n);
        int j = n - 1;
        for(int i = n - 1; i >= 0 && j >= 0; i--, j--) {
            while(b[i] < a[j] && j >= 0) j--;
            if(j >= 0) ans1++;
            else break;
        }
        ans1 = n - ans1;
        temp = 0;
        j = n - 1;
        for(int i = n - 1; i >= 0 && j >= 0; i--, j--) {
            while(b[j] > a[i] && temp <= i && j >= 0) {
                j--;
                temp++;
            }
            if(temp <= i && j >= 0) ans2++;
            else break;
        }
        printf("Case #%d: %d %d\n", cnt++, ans2, ans1);
    }
}

int main()
{
    // freopen("in", "r", stdin);
    // freopen("out", "w", stdout);
    run();
    return 0;
}
