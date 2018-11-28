#include<iostream>
#include<string.h>
using namespace std;
int const MAX_T = 1000;
int main(){
    int T,i,j,k;
    int xCountX[4],oCountX[4],xCountY[4],oCountY[4],xCountD[2],oCountD[2];
    cin>>T;
    string map[MAX_T][4];
    string result[MAX_T];
    for(i = 0; i < T; i++){ 
        for(j = 0; j < 4; j++){
            cin>>map[i][j];
        }
        cin.get();
    }

    for(i = 0; i < T; i++){
        for(j = 0;j< 4; j++){
            xCountX[j] = 0;
            oCountX[j] = 0;
            xCountY[j] = 0;
            oCountY[j] = 0;
            xCountD[j/2] = 0;
            oCountD[j/2] = 0;
        }

        for(j = 0; j < 4; j++){
            for(k = 0; k < 4; k++){
                switch(map[i][j][k]){
                    case 'O':
                        oCountX[j]++;
                        oCountY[k]++;
                        if(k == j)
                            oCountD[0]++;
                        else if(k == 3-j)
                            oCountD[1]++;
                        break;
                    case 'X':
                        xCountX[j]++;
                        xCountY[k]++;
                        if(k == j)
                            xCountD[0]++;
                        else if(k == 3-j)
                            xCountD[1]++;
                        break;
                    case 'T':
                        oCountX[j]++;
                        oCountY[k]++;
                        xCountX[j]++;
                        xCountY[k]++;
                        if(k == j){
                            xCountD[0]++;
                            oCountD[0]++;
                        }
                        else if(k == 3-j){
                            xCountD[1]++;
                            oCountD[1]++;
                        }
                        break;
                }
            }
        }
        result[i] = "";
        for(j = 0;j< 4; j++){
            if(xCountX[j]> 3 || xCountY[j] > 3 || xCountD[j>2?1:0] > 3){
                result[i] = "X won";
                break;
            }
            if(oCountX[j] > 3 || oCountY[j] > 3 || oCountD[j>2?1:0] > 3){
                result[i] = "O won";
                break;
            }
        }

        if(result[i] == ""){
            for(j = 0; j< 4; j++){
                if((int)map[i][j].find('.') >= 0){
                    result[i] = "Game has not completed";
                    break;
                }
            }
        }

        if(result[i] == "")
            result[i] = "Draw";
    }

    for(i = 0; i < T; i++){
        cout<<"Case #"<<i+1<<": "<<result[i]<<endl;
    }
    return 0;
}
