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

int main(){
    int tt; scanf("%d",&tt);
    for (int ti=1;ti<=tt;ti++){
        int n,m; scanf("%d%d",&n,&m);
            
        int a[n][m], b[n][m];
        bool ans = false;

        memset(b, 0, sizeof(b));

        for (int i=0;i<n;i++){
            for (int j=0;j<m;j++){
                scanf("%d", &a[i][j]);
            }
        }

        for (int i=0;i<n;i++){
            int t = a[i][0];
            bool valid = true;
            for (int j=1;j<m;j++){
                if (a[i][j] > t){
                    valid = false;
                }
            }
            if (valid){
                for (int j=0;j<m;j++){
                    if (a[i][j] == t){
                        b[i][j] = 1;
                    }
                }
            }
        }

        for (int j=0;j<m;j++){
            int t = a[0][j];
            bool valid = true;
            for (int i=1;i<n;i++){
                if (a[i][j] > t){
                    valid = false;
                }
            }
            if (valid){
                for (int i=0;i<n;i++){
                    if (a[i][j] == t){
                        b[i][j] = 1;
                    }
                }
            }
        }

        // if highest in row/col
        for (int i=0;i<n;i++){
            for (int j=0;j<m;j++){
                if (b[i][j]) continue;
                int t = a[i][j];
                bool is_max = true;
                for (int k=0;k<n;k++){
                    if (t < a[k][j]) is_max = false;
                }
                if (is_max) b[i][j] = true;

                if (b[i][j]) continue;
                is_max = true;
                for (int k=0;k<m;k++){
                    if (t < a[i][k]) is_max = false;
                }
                if (is_max) b[i][j] = true;
            }
        }

        ans = true;
        for (int i=0;i<n;i++){
            for (int j=0;j<m;j++){
                if (b[i][j] == 0) ans = false;
            }
        }

        printf("Case #%d: %s\n",ti,ans?"YES":"NO");
    }
    return 0;
}

