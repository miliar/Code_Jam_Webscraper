#include <iostream>
#include <string>
#include <cstring>
using namespace std;

int T[26];
int C[10];

void find(int i, char c, string name) {
    
    int minn = 5000;
    for(int j=0; j<name.size(); j++) {
        minn = min(minn, T[name[j]-'A']);
    }
    
//    cout << " " << i << " " << minn << endl;
    C[i] = minn;
    for(int j=0; j<name.size(); j++) {
        T[name[j]-'A'] -= minn;
    }
}

int main() {
    int tests; cin >> tests;
    for(int test=1; test<=tests; test++) {
        string s; cin >> s;
        
        memset(T, 0, sizeof T);
        for(int i=0; i<s.size(); i++) {
            T[s[i]-'A']++;
        }
        
        find(0, 'Z', "ZERO");
        find(6, 'X', "SIX");
        find(7, 'S', "SEVEN");
        find(5, 'V', "FIVE");
        find(4, 'F', "FOUR");
        find(2, 'W', "TWO");
        find(8, 'G', "EIGHT");
        find(3, 'T', "THREE");
        find(1, 'O', "ONE");
        find(9, 'N', "NINE");
        cout << "Case #" << test << ": ";
        
        for(int i=0; i<26; i++) {
            if (T[i])
                cout << (char)(i+'A') << "ERROR ";
        }
        
        for(int i=0; i<=9; i++) {
            for(int j=0; j<C[i]; j++)
                cout << i;
        }
        
        cout << endl;
    }
}
