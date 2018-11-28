#include <iostream>
#include <vector>
#include <string>
#include <bits/stdc++.h>
using namespace std;

int main(){
    //freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-large.in", "r", stdin);
    //freopen("Input.txt", "r", stdin);
    freopen("OutputB.txt", "w", stdout);
    int T;
    cin>>T;
    string S;
    for(int i=1;i<=T;i++){
        cin>>S;
        int l = S.size();
        if(l==1){
            if(S[0] == '+')
                cout<<"Case #"<<i<<": "<<0<<endl;
            else
                cout<<"Case #"<<i<<": "<<1<<endl;
            continue;
        }
        char prev_char = S[0];
        int steps = 0;
        for(int j=1;j<l;j++){
           if(S[j] == '+') {
                if(prev_char == '-')
                    steps++;
                prev_char = '+';
           }
           else{
                if(prev_char == '+')
                    steps++;
                prev_char = '-';
           }

        }
        if(prev_char == '-')
            steps++;
         cout<<"Case #"<<i<<": "<<steps<<endl;
    }
    return 0;
}
