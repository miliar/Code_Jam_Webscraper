#include<iostream>
#include<string>

using namespace std;

string flip(string& s){
    for(int x = 0; x < s.length(); ++x){
        if(s[x] == '+'){
            s[x] = '-'; 
        } else {
            s[x] = '+'; 
        }
    }
    return s;
}

string flip(string& s, int y){
    for(int x = 0; y>=x ;--y){
        if(s[y] == '+'){
            s[y] = '-';
        } else {
            s[y] = '+'; 
        } 
    }
    return s;
}

int findDeepest(string& s){
    for(int x = s.length()-1; x >= 0; --x){
        if(s[x] == '-'){
            return x; 
        }
    }
    return -1;
}

int exec(string& s){
    int x = findDeepest(s);
    int counter = 0;
    while(x != -1){
        s = flip(s, x); 
        x = findDeepest(s);
        ++counter;
    }
    return counter;
}

void m(){
    int junk;
    cin >> junk;
    string val;
    int counter = 1;
    while(cin >> val){
        cout << "Case #" << counter << ": " << exec(val) << endl;
        ++counter;
    }
}

int main(){
    m();
}
