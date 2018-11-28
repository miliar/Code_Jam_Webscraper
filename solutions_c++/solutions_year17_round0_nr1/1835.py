#include <bits/stdc++.h>
using namespace std;



void process(){
    int K;
    string s;
    cin>>s>>K;
    int valasz = 0;
    queue<int> akt_forditasok;
    for(int i=0; i<s.size(); i++){
        //cout<<i<<", ";
        while(!akt_forditasok.empty() && akt_forditasok.front() <= i) akt_forditasok.pop();
        bool akt = (akt_forditasok.size() + (s[i] == '+'))%2;
        if(!akt){
            if(i+K > s.size()){
                //cout<<s.size()<<" ";
                cout<<"IMPOSSIBLE";
                return;
            }
            //cout<<"jepp";
            valasz++;
            akt_forditasok.push(i+K);
        }
    }
    cout<<valasz;
}


int main(){
    ios_base::sync_with_stdio(false);
    freopen("A-large.in", "r", stdin);
    freopen("vegpal.txt", "w", stdout);
    int T;
    cin>>T;
    for(int i=1; i<=T; i++){
        cout<<"Case #"<<i<<": ";
        process();
        cout<<endl;
    }
}
