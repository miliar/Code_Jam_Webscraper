#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(){
    string S = "";
    string temp = "";

    string res = "";

    int T;
    cin >> T;
    string data[T];

    for(int t = 0; t < T; t++){
        temp = "";
        cin >> S;
        temp += S[0];

        for(int n = 1; n < S.length(); n++){
            if(S[n] < temp[0])
                temp += S[n];
            else
                temp = S[n] + temp;
        }

        data[t] = temp;
    }

    for(int n = 0; n < T; n++)
        cout << "Case #" << (n+1) << ": "  << data[n]  << endl;

    return 0;
}
