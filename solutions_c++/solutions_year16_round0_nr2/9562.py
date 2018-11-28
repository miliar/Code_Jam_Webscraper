#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int main(){
    int t;
    string s;
    cin >> t;
    for(int i = 1; i <= t; i++){
        cin >> s;
        int ans = 0;
        int pre = 0;
        do{
            pre++;
            //puts("------------------------");
            int len = s.size(), idx = -1;
            for(int x = len - 1; x >= 0; x--){
                if(s[x] == '-'){
                    idx = x + 1;
                    break;
                }
            }
            if(idx == -1)
                break;
            ans++;
            string newS = "";
            for(int x = 0; x < idx; x++)
                newS += s[x];

            //cout << s << " -> " << newS << endl;
            s = newS;
            if(newS[0] == '-'){
                reverse( s.begin(), s.end() );
                for(int x = 0 ; x < idx; x++){
                    if(s[x] == '-')
                        s[x] = '+';
                    else
                        s[x] = '-';
                }
                //cout << "opt1 " << s << endl;
            } else{
                for(int x = 0; x < idx; x++){
                    if(s[x] == '-')
                        break;
                    s[x] = '-';
                }
                //cout << "opt 2 " << s << endl;
            }
        }while(pre < 200);
        cout << "Case #" << i<< ": " << ans << endl;
    }
    return 0;
}
