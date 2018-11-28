#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<cstring>
#include<string>
using namespace std;

int a1[4][4];
int a2[4][4];
int T, c1, c2;

int main(){
    cin >> T;
    int kk = 0; 
    int ans;
    while (T--){
        kk ++;
        cin >> c1;
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j)
                cin >> a1[i][j];
        cin >> c2;
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j)
                cin >> a2[i][j];
        int count = 0; 
        for (int k = 1; k < 17; ++k){  // check if number k satisfies
            bool flag = 0;
            bool flag2 = 0;
            for (int i =0; i < 4; ++i){
                if (a1[c1-1][i] == k) flag = 1;
                if (a2[c2-1][i] == k) flag2 = 1;
            }
            if (flag & flag2){
                count ++;
                ans = k;
            }
        }
        if (count == 0) printf("Case #%d: Volunteer cheated!\n", kk);
        else if (count > 1) printf("Case #%d: Bad magician!\n", kk);
        else printf("Case #%d: %d\n", kk, ans);
    }
}
