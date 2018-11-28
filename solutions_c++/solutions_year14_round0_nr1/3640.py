#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;
ifstream fin("magictrick.in"); ofstream fout("magictrick.out");

int main(){
    int T;
    fin >> T;
    for(int cases = 1; cases <= T; cases++){
        int row, temp;
        bool nums[17];
        memset(nums, 0, sizeof(nums));
        fin >> row;
        for(int i = 1; i <= 4; i++){
            for(int j = 0; j < 4; j++){
                fin >> temp;
                if(i == row) nums[temp] = true;
            }
        }
        fin >> row;
        int ans = -1, cnt = 0;
        for(int i = 1; i <= 4; i++){
            for(int j = 0; j < 4; j++){
                fin >> temp;
                if(i == row && nums[temp]){
                        ans = temp;
                        cnt++;
                }
            }
        }
        if(cnt == 0){
            fout << "Case #" << cases << ": Volunteer cheated!\n";
        }
        if(cnt == 1){
            fout << "Case #" << cases << ": " << ans << endl;
        }
        if(cnt > 1){
            fout << "Case #" << cases << ": Bad magician!\n";
        }
    }
}
