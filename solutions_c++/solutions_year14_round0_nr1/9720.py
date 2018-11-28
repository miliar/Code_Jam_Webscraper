#include <iostream>
#include <fstream>
#include <math.h>
#include <string>
#include <cmath>
#include <stdio.h>
#include <stdlib.h>
//#include <gmpxx.h>


using namespace std;

#define dimen 101

int first[4],second[4];
int v1[4][4],v2[4][4];
int n,firstchose,secondchose;

int main(){
    #ifndef ONLINE_JUDGE
        freopen("A-small-attempt0.in", "r", stdin);
        freopen("test.out", "w", stdout);
    #endif

    scanf("%d", &n);
    for (int i=0;i<n;++i){
        cin >> firstchose;
        for (int j=0; j<4;++j){
            for (int k=0;k<4;++k){
                cin >> v1[j][k];
            }
        }
        for(int j=0;j<4;++j){
            first[j] = v1[firstchose-1][j];
        }
        cin >> secondchose;
        for (int j=0; j<4;++j){
            for (int k=0;k<4;++k){
                cin >> v2[j][k];
            }
        }
        for(int j=0;j<4;++j){
            second[j] = v2[secondchose-1][j];
        }
        int nr=0;
        int ans=0;
        for(int k=0;k<4;++k){
            for(int j=0;j<4;++j){
                if (first[k] == second[j]){
                    ans = first[k];
                    nr++;
                }
            }
        }

        if (nr == 0){
            cout << "Case #" << i+1 << ": Volunteer cheated!\n";
        }
        else if (nr>1){
            cout << "Case #" << i+1 << ": Bad magician!\n";
        }
        else if (nr==1){
            cout << "Case #" << i+1 << ": " << ans << "\n";
        }
    }
    return 0;
}
