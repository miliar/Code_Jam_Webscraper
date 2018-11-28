#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int data_1[4][4];
int data_2[4][4];

int solve(int r1, int r2){
    int num = 0;
    int rec = 0;
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            if(data_1[r1-1][i] == data_2[r2-1][j]){
                num++;
                rec = data_1[r1-1][i];
            }
        }
    }
    if(num == 0){
        cout << "Volunteer cheated!" << endl;
    }
    else if(num == 1){
        cout << rec << endl;
    }
    else{
        cout << "Bad magician!" << endl;
    }
}
int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T, cas = 0;
    scanf("%d", &T);
    while(T--){
        printf("Case #%d: ", ++cas);
        int row_1, row_2;
        scanf("%d", &row_1);
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                scanf("%d", &(data_1[i][j]));
                //cout << data_1[i][j] << " ";
            }
            //cout << endl;
        }
        scanf("%d", &row_2);
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                scanf("%d", &(data_2[i][j]));
                //cout << data_1[i][j] << " ";
            }
            //cout << endl;
        }
        solve(row_1, row_2);
    }
    return 0;
}
