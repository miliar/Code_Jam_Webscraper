#include <bits/stdc++.h>
#include <cstdio>

using namespace std;

int main(){

    freopen("A-large.in", "r", stdin);
    freopen("output4.txt", "w", stdout);
    int tt;
    cin>>tt;

    for(int ttt = 1; ttt <= tt; ttt++){
        string s;
        int k;
        cin>>s>>k;

        int res = 0;
        for(int i = 0; i < s.size(); i++){

            if(s[i] == '-'){
                if((i + k  - 1)< s.size()){
                    for(int j = i; j < i + k; j++){
                        if(s[j] == '-') s[j] = '+';
                        else s[j] = '-';
                    }
                }
                else{
                    res = -1;
                    break;
                }

                res++;
            }
        }

        cout<<"Case #"<<ttt<<": ";
        if(res != -1){
            cout<<res<<endl;
        }
        else{
            cout<<"IMPOSSIBLE"<<endl;
        }
    }

    return 0;
}
