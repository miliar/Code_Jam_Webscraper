#include <iostream>
#include <string>
using namespace std;

int main(){
    int T;
    cin >> T;
    for(int i=1;i<=T;++i){
        int R,X,C;
        string s;
        cin >> X >> R >> C;
        
        if(X==1)
            s = "GABRIEL";
        if(R*C%X !=0)
            s = "RICHARD";
        else if(X==2 )
            s = "GABRIEL";
        else if(X==3){
            if(R == 1 || C == 1)
                s = "RICHARD";
            else
                s = "GABRIEL";
        }
        else if(X==4){
            if(R<4 && C < 4)
                s = "RICHARD";
            else {
                if(R<=2 || C <= 2)
                    s = "RICHARD";
                else
                    s = "GABRIEL";
            }
        }
            
            
        
        cout << "Case #" << i << ": "<< s << endl;
    }
        
    return 0;
}
