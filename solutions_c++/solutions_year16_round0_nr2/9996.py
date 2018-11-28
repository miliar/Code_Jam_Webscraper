//
// Created by 王若璇 on 16/4/9.
//
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <vector>
#include <cmath>
#include <queue>
using namespace std;
int nums=0;
void solve(string &s){
    int i;
    char now;
    for(i = 0;i<s.length();i++){
        now = s[i];
        while (s[i]==now&&i<s.length()){
            i++;
        }
        if(i<s.length()&&s[i]!=now){
            nums++;
        }
        i--;
    }
    if(now=='-'){
        nums++;
    }
}
void filp(string &s,int begin,int end){
    for(int i = begin;i<=end;i++){
        if(s[i]=='+'){
            s[i]='-';
        } else{
            s[i]='+';
        }
    }

}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int tCase;
    int tID = 0;
    cin>>tCase;
    string s;
    vector<int> p;
    while (tCase--){
        cin>>s;
        cout<<"Case #"<<++tID<<": ";
        nums = 0;
        solve(s);
        cout<<nums<<endl;

    }
    return 0;
}