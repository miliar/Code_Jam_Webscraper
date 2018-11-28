#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int rec(string s) {
    if(s.length() == 0) return 0;
    int i = s.length()-1;
    for( ;i>=0;i--) {
        if(s[i] != '+') break;
    }
    if(i==-1) return 0;
    int j = 0;
    for(;j<=i;j++) if(s[j] == '-') break;
    int k = j;
    for(;k<=i;k++) if(s[k] == '+') break;
    string t;
    for(int l=k;l<=i;l++) {
        if(s[l] == '+') t += '-';
        else t += '+';
    }
    reverse(t.begin(),t.end());
    if(s[0] == '-') {
        return 1+rec(t);
    } else {
        return 2+rec(t);
    }
}

int main()
{
    int T;
    cin >> T;
    for(int caseno=1;caseno<=T;caseno++) {
        string s;
        cin >> s;
        int ret = rec(s);
        cout << "Case #" << caseno << ": " << ret << endl;
    }
}
