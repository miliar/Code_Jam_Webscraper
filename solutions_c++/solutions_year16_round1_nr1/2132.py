#include <bits/stdc++.h>
#include <iostream>
#include <string>
using namespace std;


int main(){
    freopen("output.txt", "w", stdout);
    freopen("input.in", "r", stdin);
    int t;
    cin>>t;
    for(int qq=1;qq<=t;qq++){
        cout<<"Case #"<<qq<<": ";
        string s;
        cin>>s;
        
        string x;
        x += s[0];
//        cout<<x;
        for(int i=1;i<s.length(); i++){
            if(s[i] >= x[0]){
                char ch = s[i];
                x.insert(x.begin(),ch);
            }else{
                x += s[i];
            }
        }
        cout<<x<<endl;
        
    }
    return 0;
}