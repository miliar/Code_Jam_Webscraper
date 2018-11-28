#include<iostream>
#include<string>

using namespace std;

int main(){
    std::ios::sync_with_stdio(false);
    int t;
    cin >> t;
    for(int itrS = 0; itrS < t; itrS++){
        string str;
        cin >> str;
        string out;
        char f = 'A', l = 'Z';
        for(int i = 0; i < str.length(); i++){
            if(str.at(i) >= f){ 
                out = str.at(i) + out;
                f = str.at(i);
            }
            else    out = out + str.at(i);
        }
        cout << "Case #" << itrS + 1 << ": " << out << endl;
    }
    return 0;
}
