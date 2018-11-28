#include<iostream>
#include<string>
#include<fstream>
using namespace std;

int main() {
    ifstream in("A-large.in",ios_base::in);
    ofstream out("out.txt",ios_base::out);
    if(in.fail() || out.fail()){
        cout << "Error" <<endl; return 0;
    }
    int cases; char tick[4][4]; bool dot = false;
    in >> cases;

    for(int k=1; k<=cases; k++) {
        dot = false;
        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                in >> tick[i][j];
                if(tick[i][j]=='.'){
                    dot=true;
                }
            }
        }
        bool found=false;
        for(int i=0; i<4; i++){
            if((tick[i][0]=='X' || tick[i][0]=='T') && (tick[i][1]=='X' || tick[i][1]=='T') && (tick[i][2]=='X' || tick[i][2]=='T') && (tick[i][3]=='X' || tick[i][3]=='T')){
                out << "Case #"<<k << ": X won" <<endl;
                found="true"; break;
            }
            if((tick[i][0]=='O' || tick[i][0]=='T') && (tick[i][1]=='O' || tick[i][1]=='T') && (tick[i][2]=='O' || tick[i][2]=='T') && (tick[i][3]=='O' || tick[i][3]=='T')){
                out << "Case #"<<k << ": O won" <<endl;
                found="true"; break;
            }
        }
        if(found==false){
             for(int i=0; i<4; i++){
                if((tick[0][i]=='X' || tick[0][i]=='T') && (tick[1][i]=='X' || tick[1][i]=='T') && (tick[2][i]=='X' || tick[2][i]=='T') && (tick[3][i]=='X' || tick[3][i]=='T')){
                    out << "Case #"<<k << ": X won" <<endl;
                    found="true"; break;
                }
                if((tick[0][i]=='O' || tick[0][i]=='T') && (tick[1][i]=='O' || tick[1][i]=='T') && (tick[2][i]=='O' || tick[2][i]=='T') && (tick[3][i]=='O' || tick[3][i]=='T')){
                    out << "Case #"<<k << ": O won" <<endl;
                    found="true"; break;
                }
             }
        }

        if(found==false){
            if((tick[0][0]=='X' || tick[0][0]=='T') && (tick[1][1]=='X' || tick[1][1]=='T') && (tick[2][2]=='X' || tick[2][2]=='T') && (tick[3][3]=='X' || tick[3][3]=='T')){
                out << "Case #"<<k << ": X won" <<endl;
                found="true";
            }
            else if((tick[0][0]=='O' || tick[0][0]=='T') && (tick[1][1]=='O' || tick[1][1]=='T') && (tick[2][2]=='O' || tick[2][2]=='T') && (tick[3][3]=='O' || tick[3][3]=='T')){
                out << "Case #"<<k << ": O won" <<endl;
                found="true";
            }
            else if((tick[0][3]=='X' || tick[0][3]=='T') && (tick[1][2]=='X' || tick[1][2]=='T') && (tick[2][1]=='X' || tick[2][1]=='T') && (tick[3][0]=='X' || tick[3][0]=='T')){
                out << "Case #"<<k << ": X won" <<endl;
                found="true";
            }
            else if((tick[0][3]=='O' || tick[0][3]=='T') && (tick[1][2]=='O' || tick[1][2]=='T') && (tick[2][1]=='O' || tick[2][1]=='T') && (tick[3][0]=='O' || tick[3][0]=='T')){
                out << "Case #"<<k << ": O won" <<endl;
                found="true";
            }
        }

        if(found==false && dot==true){
            out << "Case #"<<k << ": Game has not completed" <<endl;
        }
        if(found==false && dot==false){
            out << "Case #"<<k << ": Draw" <<endl;
        }
    }

    in.close();
    out.close();
    return 0;
}
