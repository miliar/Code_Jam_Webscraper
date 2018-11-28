#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <vector>
#include <string>
#include <queue>
#include <iostream>
using namespace std;

bool fless(double a,double b){ return b-a>1e-6; }
bool fequal(double a,double b){ return fabs(b-a)<=1e-6; }

#define N 2100
int A[N][N];

int main(){
    int tt; scanf("%d",&tt);
    for (int ti=1;ti<=tt;ti++){
        int n; scanf("%d", &n);
        int a[n], b[n];
        for (int i=0;i<n;i++) scanf("%d", &a[i]);
        for (int i=0;i<n;i++) scanf("%d", &b[i]);
        
        for (int i=0;i<n;i++) {
            for (int j=0;j<n;j++) {
                A[i][j] = 0;
            }
        }

        for (int i=1;i<n;i++) {
            //printf("processing %d\n", i);
            // find the last a[i]-1 in a
            int next_last = a[i] - 1;
            bool see[n]; memset(see, 0, sizeof(see));
            for (int j=i-1; j>=0; j--) {
                if (a[j] < a[i] && !see[a[j]]) {
                    A[j][i] = 1;
                    //printf("%d < %d\n", j, i);
                } else if (a[i] <= a[j]) {
                    A[i][j] = 1;
                    //printf("%d < %d\n", i, j);
                }
                see[a[j]]= true;
            }
        }

        for (int i=n-1;i>=0;i--) {
            int next_last = a[i]-1;
            bool see[n]; memset(see, 0, sizeof(see));
            for (int j=i+1;j<n;j++) {
                if (b[j] < b[i] && !see[b[j]]) {
                    A[j][i] = 1;
                } else if (b[i] <= b[j]) {
                    A[i][j] = 1;
                }
                see[b[j]] = true;
            }
        }

        /*
        for (int i=0;i<n;i++){
            for (int j=0;j<n;j++)printf("%d", A[i][j]);
            puts("");
        }
        */


        // tsort
        int ANS[n];
        int deg[n];
        int vis[n]; 
        int val[n];
        memset(vis,0,sizeof(vis));
        memset(deg,0,sizeof(deg));

        for (int i=0;i<n;i++) {
            for (int j=0;j<n;j++) {
                if (A[i][j]) deg[j]++;
            }
        }

        for (int i=0;i<n;i++) {
            //for (int j=0;j<n;j++) printf("%d ", deg[j]); puts("");
            for (int j=0;j<n;j++) {
                if (deg[j]==0 && !vis[j]) {
                    vis[j] = true;
                    ANS[i] = j;
                    val[j] = i + 1;
                    for (int k=0;k<n;k++) {
                        if (A[j][k]) {
                            A[j][k] = 0;
                            deg[k]--;
                        }
                    }
                    break;
                }
            }
        }
        
        int ans = 0;
        printf("Case #%d:",ti);
        for (int i=0;i<n;i++)printf(" %d", val[i]); puts("");
    }
    return 0;
}
