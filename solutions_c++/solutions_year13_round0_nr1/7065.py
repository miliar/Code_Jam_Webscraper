#include <iostream>
#include <vector>
#include <string>

using namespace std;

int T;

bool s(char& c,vector<string> v,int px,int py,int vx,int vy){
    c = ' ';
    for(int i=0;i<4;i++){
        if(v[py][px] == '.'){
            c = 'd';
            return false;
        }
        if(c != ' ' && v[py][px] != 'T' && v[py][px] != c){
            c = 'd';
            return false;
        }
        if(c == ' ' && v[py][px] != 'T'){
            c = v[py][px];
        }
        px += vx;
        py += vy;
    }
    return c;
}

string solve(vector<string> v){
    char c = ' ';
    string str;
    for(int i=0;i<4;i++){
        if(s(c,v,i,0,0,1)){
            str = string() + c + " won";
            return str;
        }
    }
    for(int i=0;i<4;i++){
        if(s(c,v,0,i,1,0)){
            str = string() + c + " won";
            return str;
        }
    }
    if(s(c,v,0,0,1,1)){
        str = string() + c + " won";
        return str;
    }
    if(s(c,v,0,3,1,-1)){
        str = string() + c + " won";
        return str;
    }
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            if(v[i][j] == '.'){
                return "Game has not completed";
            }
        }
    }
    return "Draw";
}

int main(){
    cin >> T;
    vector<string> v;
    string a;
    for(int i=1;i<=T;i++){
        v.clear();
        for(int j=0;j<4;j++){
            cin >> a;
            v.push_back(a);
        }
        string s = solve(v);
        cout << "Case #" << i << ": " << s << endl;
    }
}
