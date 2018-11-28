#include <iostream>
#include <fstream>
using namespace std;

int main(){
    freopen("D-small-attempt3.in","r",stdin);
    freopen("D-small-attempt3.out","w",stdout);
    int T;
    cin >> T;
    int X,R,C;
    for(int t=0; t<T; t++){
        cin >> X >> R >> C;

        bool rich=false;
        if(X==1){
            rich = false;
        }
        else if(X==2){
            if(R==1 && C==1)    rich = true;
            if(R==1 && C==3)    rich = true;
            if(R==3 && C==1)    rich = true;
            if(R==3 && C==3)    rich = true;
        }
        else if(X==3){
            if(R==1 && C==1)    rich = true;
            if(R==1 && C==2)    rich = true;
            if(R==2 && C==1)    rich = true;
            if(R==1 && C==3)    rich = true;
            if(R==3 && C==1)    rich = true;
            if(R==1 && C==4)    rich = true;
            if(R==4 && C==1)    rich = true;
            if(R==2 && C==2)    rich = true;
            if(R==2 && C==4)    rich = true;
            if(R==4 && C==2)    rich = true;
            if(R==4 && C==4)    rich = true;
        }
        else if(X==4){
            rich = true;
            if(R==3 && C==4)    rich = false;
            if(R==4 && C==3)    rich = false;
            if(R==4 && C==4)    rich = false;
        }
        if(rich)
            cout << "Case #" << t+1 << ": " << "RICHARD" << endl;
        else
            cout << "Case #" << t+1 << ": " << "GABRIEL" << endl;
    }
    return 0;
}
