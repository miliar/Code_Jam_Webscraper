#include <iostream>

using namespace std;

string Go(){
    int x, r, c;
    cin >> x >> r >> c;
    if(x==1)return "GABRIEL";
    if(x==2){
        if(r*c%2!=0)return "RICHARD";
        else return "GABRIEL";
    }
    if(x==3){
        if(r*c%3!=0 || (r==1 && c==3) || (r==3 && c==1))return "RICHARD";
        else return "GABRIEL";
    }
    if(x==4){
        if(r*c%4!=0 || (r==1 && c==4) || (r==4 && c==1) || (r==2 && c==4) || (r==4 && c==2) || (r==2 && c==2)){
            return "RICHARD";
        }
        else return "GABRIEL";
    }
}

int main(){
    int t;
    cin >> t;
    for(int q = 0; q < t; q++){
        string str = Go();
        cout << "Case #" << q+1 << ": " << str << "\n";

    }
}
