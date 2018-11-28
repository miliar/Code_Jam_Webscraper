#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
     int cases=0;
     fstream cin("b");
    ofstream cout("br");
    string s;
    cin>>t;
    while(t--){
    cases++;
    cin>>s;
    stack<char> Q;
    for(int i=0;i<s.size();i++){
    Q.push(s[i]);
    }


    char auxi='+';
    char focus='-';
    char aux='+';
    int consts=0;
    while(!Q.empty()){
    char h=Q.top();
    Q.pop();
   // cout<<h<<" "<<focus<<endl;
    if(h==focus){
    consts++;
    auxi=focus;
    focus=aux;
    aux=auxi;
    }


    }
    cout<<"Case #"<<cases<<": "<<consts<<endl;

    }
    return 0;
}
