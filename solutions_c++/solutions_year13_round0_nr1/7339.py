#include<iostream>
#include<cstring>
using namespace std;

int main() {

    int T;
    cin>>T;

    for(int t=1; t<=T; t++) {
        char ticToe[4][4];
        int winner =0;
        for(int i=0; i<4; i++) {
            cin>>ticToe[i];
        }

        //horizontal check
        for(int i=0; i<4; i++)
        {
            char temp[5]={ticToe[i][0], ticToe[i][1], ticToe[i][2], ticToe[i][3], '\0'};
            
            if(!strcmp(temp, "XXXX") || !strcmp(temp, "TXXX") ||
               !strcmp(temp, "XTXX") || !strcmp(temp, "XXTX") ||
               !strcmp(temp, "XXXT"))
            {
                cout<<"Case #"<<t<<": X won\n";
                winner =1;
            }
            else if(!strcmp(temp, "OOOO") || !strcmp(temp, "TOOO") ||
               !strcmp(temp, "OTOO") || !strcmp(temp, "OOTO") ||
               !strcmp(temp, "OOOT"))
            {
                cout<<"Case #"<<t<<": O won\n";
                winner =1;
            }
        }

        if(winner) continue;
        //vertical check
        char ticToeVert[4][4] = {{ticToe[0][0], ticToe[1][0], ticToe[2][0], ticToe[3][0]},
                                 {ticToe[0][1], ticToe[1][1], ticToe[2][1], ticToe[3][1]},
                                 {ticToe[0][2], ticToe[1][2], ticToe[2][2], ticToe[3][2]},
                                 {ticToe[0][3], ticToe[1][3], ticToe[2][3], ticToe[3][3]}
                                };
        for(int i=0; i<4; i++)
        {
            char temp[5]={ticToeVert[i][0], ticToeVert[i][1], ticToeVert[i][2], ticToeVert[i][3], '\0'};
            
            if(!strcmp(temp, "XXXX") || !strcmp(temp, "TXXX") ||
               !strcmp(temp, "XTXX") || !strcmp(temp, "XXTX") ||
               !strcmp(temp, "XXXT"))
            {
                cout<<"Case #"<<t<<": X won\n";
                winner =1;
            }
            else if(!strcmp(temp, "OOOO") || !strcmp(temp, "TOOO") ||
               !strcmp(temp, "OTOO") || !strcmp(temp, "OOTO") ||
               !strcmp(temp, "OOOT"))
            {
                cout<<"Case #"<<t<<": O won\n";
                winner =1;
            }
        }

        if(winner) continue;
        //diagonal check
        char ticToeD1[5] = {ticToe[0][0], ticToe[1][1], ticToe[2][2], ticToe[3][3], '\0'};
        char ticToeD2[5] = {ticToe[0][3], ticToe[1][2], ticToe[2][1], ticToe[3][0], '\0'};
        
        if(!strcmp(ticToeD1, "XXXX") || !strcmp(ticToeD1, "TXXX") ||
               !strcmp(ticToeD1, "XTXX") || !strcmp(ticToeD1, "XXTX") ||
               !strcmp(ticToeD1, "XXXT"))
        {
            cout<<"Case #"<<t<<": X won\n";
            winner =1;
        }
        else if(!strcmp(ticToeD1, "OOOO") || !strcmp(ticToeD1, "TOOO") ||
                !strcmp(ticToeD1, "OTOO") || !strcmp(ticToeD1, "OOTO") ||
                !strcmp(ticToeD1, "OOOT"))
        {
            cout<<"Case #"<<t<<": O won\n";
            winner =1;
        }
        else if (!strcmp(ticToeD2, "XXXX") || !strcmp(ticToeD2, "TXXX") ||
               !strcmp(ticToeD2, "XTXX") || !strcmp(ticToeD2, "XXTX") ||
               !strcmp(ticToeD2, "XXXT"))
        {
            cout<<"Case #"<<t<<": X won\n";
            winner =1;
        }
        else if(!strcmp(ticToeD2, "OOOO") || !strcmp(ticToeD2, "TOOO") ||
           !strcmp(ticToeD2, "OTOO") || !strcmp(ticToeD2, "OOTO") ||
           !strcmp(ticToeD2, "OOOT"))
        {
            cout<<"Case #"<<t<<": O won\n";
            winner =1;
        }

        //check for not being a game
        if(winner ==0) {
                  int complete =1;
            for(int i=0;i<4;i++) {
                if(strstr(ticToe[i], ".")){
                    cout<<"Case #"<<t<<": Game has not completed\n";
                    complete =0;
                    break;
                }
            }
            if(complete) {
            cout<<"Case #"<<t<<": Draw\n";
            }
            
        } 
    }
    
    return 0;
}
