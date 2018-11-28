#include <iostream>
#include <string>

using namespace std;

const char PLUS = '+';
const char MINUS = '-';

bool done(const string &s) {
    return s.find(MINUS) == string::npos;
}

char flip(char c){
    return c == PLUS? MINUS : PLUS;
}

void flip(string &s, int end){
    char c = flip(s[0]);
    fill(s.begin(), s.begin() + end, c);
}

void comp(int tc){
    string s;
    cin >> s;
    
    int res = 0;
    while(!done(s)){
        auto idx = s.find(flip(s[0]));
        if(idx == string::npos)
            idx = s.size();
        flip(s, (int)idx);
        ++res;
    }
    cout << "Case #" << tc << ": " << res << endl;
}

int main(){
    int T;
    cin >> T;
    for(int i=1; i<=T; ++i){
        comp(i);
    }
}