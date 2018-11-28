#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;


int main(int argc, char *argv[])
{
    ifstream fcin("A-small-attempt0.in");
    ofstream fcout("ans.txt");
    int T; fcin >> T;
    for(int i = 1; i <= T; i++){
            int common[17] = {};
            for(int ask = 0; ask < 2; ask++){
                int ans; fcin >> ans;
                int num[4][4];
                for(int j = 0; j < 4; j++){
                        for(int k = 0; k < 4; k++){
                                fcin >> num[j][k];
                                if(ans == j+1){
                                       common[num[j][k]]+=1;
                                }        
                        }        
                }
            }
            int cnt2 = 0;
            int ret = -1;
            for(int j = 1; j <= 16; j++){
                    if(common[j]==2){
                         cnt2 += 1;
                         ret = j;
                    }      
            }
            if(cnt2 == 1){
                 fcout << "Case #" << i << ": " << ret << endl; 
            } else if(cnt2 == 0){
                 fcout << "Case #" << i << ": Volunteer cheated!" << endl;
            } else 
            fcout << "Case #" << i << ": Bad magician!" << endl;
                    
    } 
    system("PAUSE");
    return EXIT_SUCCESS;
}
