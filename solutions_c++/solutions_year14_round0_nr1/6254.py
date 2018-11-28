#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <cstring>
using namespace std;

//function declaraions


int main(){

    string fname = "small";
    freopen((fname+".in").c_str(), "r", stdin);
    freopen((fname+".out").c_str(), "w", stdout);// ------- needed to output to file

    //number of cases to follow
    int cases;
    scanf("%d", &cases);
    for (int i = 1; i <= cases; ++i) {
        //values about each case
        int rowa, rowb, row1[4][4], row2[4][4];
        scanf("%d",&rowa);
        for (int j = 0; j<4; j++){
            for (int aa = 0; aa<4;aa++){
                scanf("%d",&row1[j][aa]);
            }
        }
        scanf("%d",&rowb);
        for (int j = 0; j<4; j++){
            for (int aa = 0; aa<4;aa++){
                scanf("%d",&row2[j][aa]);
            }
        }
        int same = 0;
        int num;
        for (int z = 0;z<4;z++){
            for (int y = 0; y<4;y++){
                if (row1[rowa-1][z] == row2[rowb-1][y]){
                    same++;
                    num = row1[rowa-1][z];
                }
            }
        }
        
        printf("Case #%d: ", i);
        if (same == 0){
            cout<<"Volunteer cheated!";
        }else if (same == 1){
            cout<<num;
        }else{
            cout<<"Bad magician!";
        }
        cout<<endl;

    }

    return 0;
}
