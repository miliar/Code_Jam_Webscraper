#include <iostream>
#include <algorithm>
#include <string>
#include <iostream>

using namespace std;

int main(){
    int T;
    cin >> T;
    int CN = 0;
    while(T--){
        ++CN;
        string s;
        cin >> s;
        string out = s.substr(0, 1);
        for(int i=1; i<s.size(); i++){
            if(s[i] >= out[0]){
                out = s.substr(i, 1) + out;
            }
            else{
                out += s.substr(i, 1);
            }
        }
        cout << "Case #" << CN << ": " << out << endl;
    }
}
