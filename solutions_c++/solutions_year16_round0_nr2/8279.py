#include <bits/stdc++.h>

using namespace std;

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, temp=0;
    cin >> t;
    while(t--){
        string s;
        cin >> s;
        int a=0;
        if(s.length()==1){
            if(s[0]=='+')
                cout << "Case #" << ++temp << ": 0" << endl;
            else
                cout << "Case #" << ++temp << ": 1" << endl;
        }
        else{
            a=0;
            for(int i=0; i<s.length()-1; i++){
                if(s[i]!=s[i+1]){
                    a++;
                }
            }
            if(s[s.length()-1]=='-'){
                a++;
            }
            cout << "Case #" << ++temp << ": " << a << endl;
        }
    }

    return 0;
}
