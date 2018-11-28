#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>


using namespace std;

char WhoWinDig1(vector<string> board,char XO){
     bool T=0;
     int ctr=0;
     for(int Q=0;Q<4;Q++){
             if(board[Q][Q]==XO){
                                 ctr++;
                                 }
             else if(board[Q][Q]=='T'){
                  T=1;
                  }
             }
             if(ctr==4||(ctr==3&&T==1)){
                                        return XO;
                                        }
             return 'N';
     }
     
char WhoWinDig2(vector<string> board,char XO){
     bool T=0;
     int ctr=0;
     for(int Q=3;Q>=0;Q--){
             if(board[3-Q][Q]==XO){
                                 ctr++;
                                 }
             else if(board[3-Q][Q]=='T'){
                  T=1;
                  }
             }
             if(ctr==4||(ctr==3&&T==1)){
                                        return XO;
                                        }
             return 'N';
     } 

char WhoWinRow(vector<string> board,char XO){
     for(int Q=0;Q<4;Q++){
             bool T=0;
             int ctr=0;
             for(int W=0;W<4;W++){
                     if(board[Q][W]==XO){
                                         ctr++;
                                         }
                     else if(board[Q][W]=='T'){
                          T=1;
                          }
                     }
             if(ctr==4||(ctr==3&&T==1)){
                                        return XO;
                                        }
             }
             return 'N';
     }

char WhoWinCol(vector<string> board,char XO){
     for(int Q=0;Q<4;Q++){
             bool T=0;
             int ctr=0;
             for(int W=0;W<4;W++){
                     if(board[W][Q]==XO){
                                         ctr++;
                                         }
                     else if(board[W][Q]=='T'){
                          T=1;
                          }
                     }
             if(ctr==4||(ctr==3&&T==1)){
                                        return XO;
                                        }
             }
             return 'N';
     }

bool NotYet(vector<string> board){
     for(int Q=0;Q<4;Q++){
             for(int W=0;W<4;W++){
                     if(board[Q][W]=='.'){
                                          return 1;
                                          }
                     }
             }
             return 0;
     }

int main()
{
    int N;
    cin >> N;
    for(int Q=0;Q<N;Q++){
            vector<string> board(4);
            for(int W=0;W<4;W++){
                    cin >> board[W];
                    }
                    if(WhoWinCol(board,'O')=='O'){
                                                  cout << "Case #" << Q << ':' << ' ' << "O won" << endl;
                                                  }
                    else if(WhoWinCol(board,'X')=='X'){
                                                  cout << "Case #" << Q << ':' << ' ' << "X won" << endl;
                                                  }                              
                    else if(WhoWinRow(board,'O')=='O'){
                                                  cout << "Case #" << Q << ':' << ' ' << "O won" << endl;
                                                  }
                    else if(WhoWinRow(board,'X')=='X'){
                                                  cout << "Case #" << Q << ':' << ' ' << "X won" << endl;
                                                  }
                    else if(WhoWinDig1(board,'O')=='O'){
                                                        cout << "Case #" << Q << ':' << ' ' << "O won" << endl;
                                                        }
                    else if(WhoWinDig1(board,'X')=='X'){
                                                        cout << "Case #" << Q << ':' << ' ' << "X won" << endl;
                                                        }
                    else if(WhoWinDig2(board,'O')=='O'){
                                                        cout << "Case #" << Q << ':' << ' ' << "O won" << endl;
                                                        }
                    else if(WhoWinDig2(board,'X')=='X'){
                                                        cout << "Case #" << Q << ':' << ' ' << "X won" << endl;
                                                        }
                    else if(NotYet(board)){
                         cout << "Case #" << Q << ':' << ' ' << "Game has not completed" << endl;
                         }
                    else{
                         cout << "Case #" << Q << ':' << ' ' << "Draw" << endl;
                         }
            }
    system("pause");
    return 0;    
}
