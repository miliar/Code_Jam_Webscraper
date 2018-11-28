#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<set>
#include<queue>
#include<map>
#include<vector>
using namespace std;
int n, t;
int a[10010];
bool cmp(int a, int b){
    return a > b;
}

int  main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w", stdout);
    int _;
    cin >> _;
    for (int __ = 1; __ <= _; ++__){
        printf("Case #%d: ", __);
        scanf("%d %d", &n, &t);
        for (int i = 0; i < n; ++i){
            scanf("%d", &a[i]);
        }
        sort(a, a + n, cmp);
        int i = 0; int j = n - 1;
        int cnt = 0;
        while (i <= j){
            if (a[i] + a[j] <= t){
                cnt ++;
                i++;
                j--;
            }else{
                cnt++;
                i++;
            }
        }
        cout << cnt << endl;
    }
    return 0;
}
