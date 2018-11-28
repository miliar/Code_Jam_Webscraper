#include <iostream>
#include <string>
#include <bits/stdc++.h>
using namespace std;
int main(){
    freopen("A-large.in", "r", stdin);
    //freopen("Input.txt", "r", stdin);
    freopen("OutputA.txt", "w", stdout);
    int T,Smax;
    unsigned long long accumulated,invited;
    string levels;
    cin>>T;
    for(int i=1;i<=T;i++){
        invited = 0;
        accumulated = 0;
        cin>>Smax>>levels;
        for(int j=0;j<=Smax;j++){
            if(accumulated<j){
                invited += (j-accumulated);
                accumulated += (j-accumulated);
            }
            accumulated += (levels[j]-'0');
        }
        cout<<"Case #"<<i<<": "<<invited<<endl;
    }
    return 0;
}
