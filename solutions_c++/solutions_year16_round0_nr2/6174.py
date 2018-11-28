#include <iostream>
#include <cstdio>

using namespace std;

int changes(string str){
    char now = str.at(0);
    int chngs = 0;
    for(int counter = 1; counter < str.length(); counter ++){
        if(str.at(counter) != now){
            chngs ++;
            now = str.at(counter);
        }
    }
    if(now == '-'){
        chngs ++;
    }
    return chngs;
}

int main()
{
    freopen("B-large (1).in" , "r" , stdin);
    freopen("myOut.txt" , "w" , stdout);
    int T;
    int res;
    cin >> T;
    string str;
    for(int counter = 1; counter <= T; counter ++){
        cin >> str;
        res = changes(str);
        cout << "Case #" << counter << ": " << res << "\n";
    }
    return 0;
}
