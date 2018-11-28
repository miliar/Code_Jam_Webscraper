#include <iostream>
#include <bits/stdc++.h>

using namespace std;

string to_string(char n){
    stringstream ss;
    ss << n;
    return ss.str();
}


int main()
{
    int T;
    cin >> T;

    freopen("A.txt","w",stdout);

    for(int i = 1; i <= T; i++){
        string s;
        cin >> s;
        string f = to_string(s[0]);
        for(int j = 1; j < s.length(); j++){
            if(s[j] >= s[0]){
                f = s[j] + f +"";
                s[0] = s[j];
            }else{
                f = f + s[j] +"";
            }
        }
        cout << "Case #" <<i<<": "<<f<< endl;
    }

    return 0;
}
