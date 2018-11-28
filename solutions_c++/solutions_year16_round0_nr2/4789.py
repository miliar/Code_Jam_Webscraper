#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

int main(){
    int t;
    cin >> t;

    int caso = 1;

    while (t--){
        int flipCount = 0;
        string s;
        cin >> s;
        while (s.find('-') != string::npos){
            size_t f;
            if (s[0] == '+'){
                f = s.find("-");
                s.replace(s.begin(),s.begin()+f,"-");
            }
            else{
                f = s.find("+");
                s.replace(s.begin(),s.begin()+f,"+");
            }
            flipCount++;
        }
        cout << "Case #" << caso++ << ": " << flipCount << '\n';
    }
    return 0;
}
