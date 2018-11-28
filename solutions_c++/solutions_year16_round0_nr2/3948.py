#include <bits/stdc++.h>

using namespace std;

int T, n, cur, ret;
string s;
int main(){
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    cin>>T;
    for(int t = 1; t <=T; ++t){
        cin>>s;
        n = s.length();
        ret = 0;
        cur = 0;
        for(int i = n-1; i>= 0; --i){
            if(s[i] == '-'){
                for(int j = 0; j <= i; ++j)
                    s[j] = ((s[j] == '-')?'+':'-');
                ret++;
            }
        }
        cout<<"Case #"<<t<<": "<<ret<<endl;
    }
    return 0;
}
