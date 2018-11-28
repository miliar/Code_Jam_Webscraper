#include <bits/stdc++.h>
#define FOR(i,a) for(i = 0; i < a; i++)
#define FR(i,a,b) for(i = a; i < b; i++)
using namespace std;

int main(){
    long long i,j,T;
    cin >> T;
    string s,s1;
    for(int test = 1; test<=T; test++){
        cin >> s;
        s1 = s[0];
        for(i = 1; i < s.length(); i++){
            if(s1+s[i]>s[i]+s1){
                s1+=s[i];
            }else{
                s1 = s[i] + s1;
            }
        }
        cout << "Case #" << test << ": " << s1 << endl;
    }
    return 0;
}