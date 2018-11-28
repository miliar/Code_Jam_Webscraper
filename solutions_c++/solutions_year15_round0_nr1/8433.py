#include<bits/stdc++.h>

using namespace std;

int main(){

    ifstream cin("A-large.in");
    ofstream cout("A-large.out");

    int T;
    cin>>T;

    for(int t = 1; t<=T; t++){
        int x;
        string s;

        cin>>x>>s;

        int up = 0, add = 0;
        for(int i = 0; i<s.size(); i++){
            if(up < i){
                add += i - up;
                up = i;
            }
            up += s[i] - '0';
        }

        cout<<"Case #"<<t<<": "<<add<<"\n";
    }
}
