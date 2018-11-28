#include <iostream>
#include <string>

using namespace std;


int main(){
    int T;
    cin >> T;
    int m = 1;
    while(m<=T){
        string S;
        size_t pos = 0;
        string res = "";
        cin >> S;
        while(S.length() > 0){
            if(S.find('Z') < S.npos){
                while(S.find('Z') < S.npos){
                    pos = S.find('Z');
                    S.erase(pos, 1);
                    pos = S.find('E');
                    S.erase(pos, 1);
                    pos = S.find('R');
                    S.erase(pos,1);
                    pos = S.find('O');
                    S.erase(pos,1);
                    res = res + "0";
                }
            }
            else if(S.find('W') != S.npos){
                while(S.find('W') != S.npos){
                    pos = S.find('T');
                    S.erase(pos, 1);
                    pos = S.find('W');
                    S.erase(pos, 1);
                    pos = S.find('O');
                    S.erase(pos,1);
                    res = res + "2";
                }
            }
            else if(S.find('X') != S.npos){
                while(S.find('X') != S.npos){
                    pos = S.find('S');
                    S.erase(pos, 1);
                    pos = S.find('I');
                    S.erase(pos, 1);
                    pos = S.find('X');
                    S.erase(pos,1);
                    res = res + "6";
                }
            }
            else if(S.find('G') != S.npos){
                while(S.find('G') != S.npos){
                    pos = S.find('E');
                    S.erase(pos, 1);
                    pos = S.find('I');
                    S.erase(pos, 1);
                    pos = S.find('G');
                    S.erase(pos,1);
                    pos = S.find('H');
                    S.erase(pos,1);
                    pos = S.find('T');
                    S.erase(pos,1);
                    res = res + "8";
                }
            }
            else if(S.find('S') != S.npos && S.find('E') != S.npos && S.find('V') != S.npos && S.find('N') != S.npos && count(S.begin(), S.end(), 'E') >= 2){
                while(S.find('S') != S.npos && S.find('E') != S.npos && S.find('V') != S.npos && S.find('N') != S.npos && count(S.begin(), S.end(), 'E') >= 2){
                    pos = S.find('S');
                    S.erase(pos, 1);
                    pos = S.find('E');
                    S.erase(pos, 1);
                    pos = S.find('V');
                    S.erase(pos,1);
                    pos = S.find('E');
                    S.erase(pos,1);
                    pos = S.find('N');
                    S.erase(pos,1);
                    res = res + "7";
                }
            }
            else if(S.find('F') != S.npos && S.find('I') != S.npos && S.find('V') != S.npos && S.find('E') != S.npos){
                while(S.find('F') != S.npos && S.find('I') != S.npos && S.find('V') != S.npos && S.find('E') != S.npos){
                    pos = S.find('F');
                    S.erase(pos, 1);
                    pos = S.find('I');
                    S.erase(pos, 1);
                    pos = S.find('V');
                    S.erase(pos,1);
                    pos = S.find('E');
                    S.erase(pos,1);
                    res = res + "5";
                }
            }
            else if(S.find('F') != S.npos && S.find('O') != S.npos && S.find('U') != S.npos && S.find('R') != S.npos){
                while(S.find('F') != S.npos && S.find('O') != S.npos && S.find('U') != S.npos && S.find('R') != S.npos){
                    pos = S.find('F');
                    S.erase(pos, 1);
                    pos = S.find('O');
                    S.erase(pos, 1);
                    pos = S.find('U');
                    S.erase(pos,1);
                    pos = S.find('R');
                    S.erase(pos,1);
                    res = res + "4";
                }
            }
            else if(S.find('T') != S.npos && S.find('H') != S.npos && S.find('R') != S.npos && S.find('E') != S.npos && count(S.begin(), S.end(), 'E') >= 2){
                while(S.find('T') != S.npos && S.find('H') != S.npos && S.find('R') != S.npos && S.find('E') != S.npos  && count(S.begin(), S.end(), 'E') >= 2){
                    pos = S.find('T');
                    S.erase(pos, 1);
                    pos = S.find('H');
                    S.erase(pos, 1);
                    pos = S.find('R');
                    S.erase(pos,1);
                    pos = S.find('E');
                    S.erase(pos,1);
                    pos = S.find('E');
                    S.erase(pos,1);
                    res = res + "3";
                }
            }
            else if(S.find('O') != S.npos && S.find('N') != S.npos && S.find('E') != S.npos){
                while(S.find('O') != S.npos && S.find('N') != S.npos && S.find('E') != S.npos){
                    pos = S.find('O');
                    S.erase(pos, 1);
                    pos = S.find('N');
                    S.erase(pos, 1);
                    pos = S.find('E');
                    S.erase(pos,1);
                    res = res + "1";
                }
            }
            else if(S.find('N') != S.npos && S.find('I') != S.npos && S.find('E') != S.npos){
                while(S.find('N') != S.npos && S.find('I') != S.npos && S.find('E') != S.npos){
                    pos = S.find('N');
                    S.erase(pos, 1);
                    pos = S.find('I');
                    S.erase(pos, 1);
                    pos = S.find('N');
                    S.erase(pos,1);
                    pos = S.find('E');
                    S.erase(pos,1);
                    res = res + "9";
                }
            }
        }
        sort(res.begin(), res.end());
        cout <<"Case #"<< m <<": "<< res <<endl;
        m++;
    }
}