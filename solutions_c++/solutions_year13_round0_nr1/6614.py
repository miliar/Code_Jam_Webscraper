#include <iostream>
using namespace std;

int main() {
    int testpos=0;
    bool complete;
    bool xwin,owin;
    string result;
    int T; cin >> T;
    string test[10];
    char map[4][4];
    for(int t=0;t<T;++t) {
        testpos=0;
        for(int i=0;i<10;++i) test[i]="";
        complete=true; xwin=false; owin=false;
        for(int i=0;i<4;++i) {
            for(int j=0;j<4;++j) {
                cin >> map[i][j];
                if(map[i][j]=='.') complete=false;
            }
        }
        // horizontal
        for(int i=0;i<4;++i) {
            for(int j=0;j<4;++j) test[testpos]+=map[i][j];
            ++testpos;
        }
        // vertical
        for(int j=0;j<4;++j) {
            for(int i=0;i<4;++i) test[testpos]+=map[i][j];
            ++testpos;
        }
        // diagonal
        for(int i=0;i<4;++i) test[testpos]+=map[i][i]; ++testpos;
        for(int i=0;i<4;++i) test[testpos]+=map[i][3-i];
        
        for(int i=0;i<10;++i) {
            if(test[i]=="XXXX" || test[i]=="TXXX" || test[i]=="XTXX" || test[i]=="XXTX" || test[i]=="XXXT") xwin=true;
            if(test[i]=="OOOO" || test[i]=="TOOO" || test[i]=="OTOO" || test[i]=="OOTO" || test[i]=="OOOT") owin=true;
        }
        
        if(xwin) result="X won\n";
        else if(owin) result="O won\n";
        else if(!owin && !xwin && complete) result="Draw\n";
        else if(!owin && !xwin && !complete) result="Game has not completed\n";
        
        cout << "Case #" << t+1 << ": " << result;
    }
    return 0;
}
