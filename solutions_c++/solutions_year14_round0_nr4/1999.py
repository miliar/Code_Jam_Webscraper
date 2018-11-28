#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <iostream>
#define N 1005
using namespace std;

int main() {
    int i, j, t, n, ans1, ans2, T=0;
    double arr[2][N];
    int used[N];
    scanf("%d", &t);
    while(t--) {
        ans1 = ans2 = 0;
        scanf("%d", &n);
        for(i=0; i<2; i++)
            for(j=0; j<n; j++)
                scanf("%lf", &arr[i][j]);
        sort(arr[0], arr[0]+n);
        sort(arr[1], arr[1]+n);
        memset(used, 0, sizeof(used));
        int ptr=0;
        for(i=n-1; i>=0; i--) {
            int f=-1;
            for(j=n-1; j>=0; j--)
                if(!used[j] && arr[0][i]<arr[1][j]) f = j;
            if(f==-1) {
                while(used[ptr]) ptr++;
                used[ptr] = 1;
                ans1++;
            }
            else used[f] = 1;
        }
        memset(used, 0, sizeof(used));
        ptr=n-1;
        for(i=0; i<n; i++) {
            int f=-1;
            for(j=0; j<n; j++)
                if(!used[j] && arr[0][i]>arr[1][j]) f = j;
            if(f==-1) {
                while(used[ptr]) ptr--;
                used[ptr] = 1;
            }
            else used[f] = 1, ans2++;
        }

        printf("Case #%d: %d %d\n", ++T, ans2, ans1);
        /*
        puts(""); 
        for(i=0; i<n; i++) printf("%.3f ", arr[0][i]);
        puts("");
        for(i=0; i<n; i++) printf("%.3f ", arr[1][i]);
        puts("");
        */
    }
    return 0;
}
