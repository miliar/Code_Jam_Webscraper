#include<bits/stdc++.h>
#include <algorithm>
#include <string>

using namespace std;

void last_word(string str){
    if (str.length() == 0) return;
    int len = str.length();
    int max_idx = len-1;
    char c = str[len-1];
    for(int i=len-2; i >= 0; i--){
        if (str[i] > c){
            c = str[i];
            max_idx = i;
        }
        //cout << max_idx << " " << c << endl;
    }
    string sub_str = str.substr(0, max_idx);
    //cout << max_idx << " " << sub_str;
    cout << c;
    last_word(sub_str);
    cout << str.substr(max_idx+1, str.length());
}
int main(){
    int T, N, J, i;
    cin >> T;
    string str;
    i = 0;
    while (i < T){
        i++;
        cin >> str;
        cout << "Case #" << i << ": ";
        last_word(str);
        cout << endl;
    }
    return 0;
}
