#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
    int cases;
    scanf("%d", &cases);
    for(int o=1;o<=cases;o++){
        int curr[101][101] = {0};
        int a[101][101] = {0};
        int n, m;
        scanf("%d %d", &n,&m);
//        memset(curr,100, n*m);
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                scanf("%d",&a[i][j]);
                curr[i][j]=100;
            }
        }
        int mmax, mmin;
        for(int i=0;i<n;i++){
            mmax = -1;
            for(int j=0;j<m;j++){
                mmax = max(mmax, a[i][j]); 
            }
            for(int j=0;j<m;j++){
                curr[i][j] = mmax;
            }
        }
        for(int i=0;i<m;i++){
            mmin = 100;
            for(int j=0;j<n;j++){
                if(curr[j][i] != a[j][i]){
                    mmin = min (mmin, a[j][i]);
                }
            }
            for(int j=0;j<n;j++){
                if(curr[j][i] > mmin && mmin != 100){
                    curr[j][i] = mmin;
                }
            }
        }
        bool CAN = true;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(a[i][j] != curr[i][j]) {
                    CAN = false;
                    break;
                }
            }
            if( !CAN ) break;
        }
        if(CAN)
            printf("Case #%d: YES\n",o);
        else
            printf("Case #%d: NO\n",o);
    }

}
