#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

int flip(string s){
    bool flag = s[0] == '+' ? true : false;

    int i = 0;
    for(i = 1 ; i < s.size() ; ++i){
        if(flag && s[i] != '+')
            break;
        if(!flag && s[i] != '-')
            break;
    }

    if(flag && i == s.size())
        return 0;
    if(!flag && i == s.size())
        return 1;

    for(int j = 0; j < i; ++j){
        if(flag)
            s[j] = '-';
        else
            s[j] = '+';
    }
    return 1 + flip(s);


}

int main(){

int num = 0;

cin>>num;

for(int i = 0 ; i < num ;++i){
    string s;
    cin>>s;
    int ans = flip(s);
        printf("Case #%d: %d\n", i + 1, ans);
}

return 0;
}
