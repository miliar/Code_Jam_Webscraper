#include<iostream>
#include<string>
#include<fstream>

using namespace std;

#define Bad "Bad magician!"
#define Cheat "Volunteer cheated!"

ifstream fin("in");
ofstream fout("out");

int
solve(){
    int row1, row2, grid1[4][4],grid2[4][4];
    fin>>row1;
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            fin>>grid1[i][j];
        }
    }
    fin>>row2;
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            fin>>grid2[i][j];
        }
    }

    row1 -=1;
    row2 -=1;
    int flag = 0;
    int ans = 0;
    
    for(int p = 0; p < 4; p++)
    for(int q = 0; q < 4; q++){
        cout<<grid1[row1][p]<<"=="<<grid2[row2][q]<<"?"<<endl;
        if(grid1[row1][p] == grid2[row2][q]){
            flag ++;
            ans = grid1[row1][p];
        }
    }

    if(flag == 0){
        fout<<Cheat<<endl;
    } else {
        if(flag > 1){
            fout<<Bad<<endl;
        } else {
            fout<<ans<<endl;
        }
    }
    return 0;
}

int
main(){
    int case_num;
    fin >> case_num;

    for(int i = 0; i < case_num; i++){
        fout<<"Case #"<<i+1<<": ";//<<solve()<<endl;
        solve();
    }

    return 0;
}
