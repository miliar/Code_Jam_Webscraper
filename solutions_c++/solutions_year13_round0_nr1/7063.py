#include<iostream>
#include<conio.h>
#include<stdio.h>
#include<fstream>

using namespace std;

int main() {
    fflush(stdout);
    fflush(stdin);


    ofstream myfile;
      myfile.open ("ans.txt");
    //char results[100][100];
    int cases=3;
    //cout<<"cases : ";
    cin>>cases;
    //cout<<"cases : "<<cases<<endl;
    for(int k=0;k<cases;k++) {

    //cout<<"case : "<<k<<endl;
    //fflush(stdout);
    //fflush(stdin);
    char board[4][4];
    for(int pr=0;pr<4;pr++)
    for(int pc=0;pc<4;pc++)
    cin>>board[pr][pc];

    //fflush(stdout);
    //fflush(stdin);

    char board1[4][4]={'O','X','X','O',
                    'X','T','X','X',
                    'X','.','.','O',
                    'O','X','X','O'};
    int flag=0;
    int win=0;
    for(int i=0;i<4;i++) {
        flag=0;
        char ch=board[0][i];
        if(ch=='T') ch=board[1][i];
        if(ch=='.') { flag=1; continue;}
        for(int j=1;j<4;j++) {
            if(board[j][i]!=ch && board[j][i]!= 'T' ) {
                flag=1;
                break;
            }
        }
        if(flag==0) {
            if(ch=='X') {
                win=0;
            } else {
                win=1;
            }
            //cout<<"Column : "<<i<<"\n";
            break;
        }
        else {
            flag=0;
            ch=board[i][0];
            if(ch=='T') ch=board[i][1];
        if(ch=='.') { flag=1; continue;}
            for(int j=1;j<4;j++) {
                if(board[i][j]!=ch && board[i][j]!= 'T') {
                    flag=1;
                    break;
                }
            }
            if(flag==0) {
                if(ch=='X') {
                    win=0;
                } else {
                    win=1;
                }
                //cout<<"row : "<<i<<"\n";
                break;
            }
            else {
                if(i==0) {
                    flag=0;
                    ch=board[0][0];
                    if(ch=='T') ch=board[1][1];
        if(ch=='.') { flag=1; continue;}
                    for(int j=1;j<4;j++) {
                        if(board[j][j]!=ch && board[j][j]!= 'T') {
                            flag=1;
                            break;
                        }
                    }

                    if(flag==0) {
                        if(ch=='X') {
                            win=0;
                        } else {
                            win=1;
                        }
                        //cout<<"Diag 1 "<<"\n";
                        break;
                    }
                }

                if(i==3) {
                    flag=0;
                    ch=board[0][3];
                    if(ch=='T') ch=board[1][2];
        if(ch=='.') { flag=1; continue;}
                    for(int j=1;j<4;j++) {
                        if(board[j][3-j]!=ch && board[j][3-j]!= 'T') {
                            flag=1;
                            break;
                        }
                    }

                    if(flag==0) {

                        if(ch=='X') {
                            win=0;
                        } else {
                            win=1;
                        }
                        //cout<<"Diag 2 "<<"\n";
                        break;
                    }

                }
            }
        }
        if(flag==0) break;
    }


    myfile << "Case #"<<k+1<<": ";
    if(flag==0) {
        if(win==0) {
        //cout<<"X won"<<endl;
        myfile << "X won\n";
        }
        else
        myfile << "O won\n";
    }
    else {
        int flag1=0;
        for(int l=0;l<4;l++)
        for(int m=0;m<4;m++)
        if(board[l][m]=='.'){
            flag1=1;
        }
        if(flag1==1)
        myfile << "Game has not completed\n";
        else
        myfile << "Draw\n";
    }

    //cout<<"case : "<<k<<endl;
    }
    myfile.close();


}
