#include<iostream>
#include<string>
#include<cstdio>
#include<vector>
using namespace std;
#define rep(a,b) for(int a = 0; a < (int)b; a++)

string onlyCool(string s){
    if(s.size() == 0){
        return "";
    }
//    cout<<"onlycool "<<s<<endl;
    string cools, nocools;
    rep(i, s.size()){
        if(s[i] == s[0]){
            cools += s[i];
        }else{
            nocools += s[i];
        }
    }
    return (cools);
}
string onlyNotCool(string s){
    if(s.size() == 0){
        return "";
    }
//    cout<<"onlyNotCool "<<s<<endl;
    string cools, nocools;
    rep(i, s.size()){
        if(s[i] == s[0]){
            cools += s[i];
        }else{
            nocools += s[i];
        }
    }
    return (nocools);
}

string solve(string s){
    if(s.size() == 0){
        return "";
    }
//    cout<<"solve " + s<<endl;
    int firstIndex = 0, lastIndex = 0;
    rep(i, s.size()){
        if(s[i] > s[firstIndex]){
            firstIndex = lastIndex = i;
        }else if(s[i] == s[firstIndex]){
            lastIndex = i;
        }
    }

    return(onlyCool(s.substr(firstIndex, lastIndex - firstIndex + 1))
           + solve(s.substr(0, firstIndex))
           + onlyNotCool(s.substr(firstIndex, lastIndex - firstIndex + 1))
           + s.substr(lastIndex + 1)
           );
}
int main(){
//    freopen("A-large.in", "r", stdin);
//    freopen("A-large.out", "w", stdout);
    int T;
    string s;
    cin>>T;
    rep(t, T){
        cout<<"Case #"<<t+1<<": ";
        cin>>s;
        cout<<solve(s)<<endl;
    }
}
