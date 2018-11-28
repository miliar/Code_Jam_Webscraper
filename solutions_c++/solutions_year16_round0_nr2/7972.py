#include<iostream>
#include<cstdio>
#include<string>
using namespace std;
#define rep(a,b) for(int a = 0; a < (int)b; a++)
int solveString(string s){
    if(s.size() == 0){
        return 0;
    }
    bool isSolved = true;
    rep(i, s.size()){
        if(s[i] == '-'){
            isSolved = false;
            break;
        }
    }
    if(isSolved){
        return 0;
    }
    string r = "";
    int last_index = s.size() - 1;
    while(last_index >= 0 and s[last_index == '+']){
        last_index--;
    }
    if(last_index != s.size() - 1){
        rep(i, last_index + 1){
            r += s[i];
        }
        return solveString(r);
    }
    r = "";
    if(s[0] == '-'){
        for(int i = s.size() - 1; i >= 0; i--){
            r += s[i];
        }
        return 1 + solveString(r);
    }


}
int main(){
    //freopen("B-large.in", "r", stdin);
    //freopen("B-large.out", "w", stdout);
    int T;
    string s;
    cin>>T;
    //cout<<"wut"<<endl;
    rep(t,T){
        cout<<"Case #"<<t + 1<<": ";
        cin>>s;
        char actual_char = s[0];
        int ans = 0;
        rep(i, s.size()){
            if(s[i] != actual_char){
                actual_char = s[i];
                ans++;
            }
        }
        cout<<ans + (s[s.size() - 1] == '-' ? 1 : 0)<<endl;
    }
}
