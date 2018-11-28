#include <iostream>
#include <stdio.h>
using namespace std;
int main(){
    freopen("B-large.in","r",stdin);
    freopen("out_large.out", "w", stdout);
    int T, cs = 1;
    cin >> T;
    while(T--){
        string s;
        cin >> s;
        int r = 0;
        bool f = false;

    for(int i = s.size() - 1; i >= 0; i--){
        if((s[i] == '-' && f == false) || (s[i] == '+' && f == true))
            r++, f = !f;
    }

        cout<<"Case #"<<cs++<<": "<<r<<'\n';
    }
    return 0;
}

