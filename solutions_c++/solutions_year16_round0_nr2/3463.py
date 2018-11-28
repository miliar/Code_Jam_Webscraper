#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("cj.in","r",stdin);
    freopen("cj.out","w",stdout);
    int t; cin >> t;
    for(int tc=1 ; tc<=t ; tc++){
        string s; cin >> s;
        int count=0;
        bool flag = true;
        char last = '+';
        for(int i=s.size()-1 ; i>=0 ; i--){
            if(s[i]=='-') flag = false;
            if(flag) continue;
            if(s[i]!=last) count++;
            last = s[i];
        }
        cout << "Case #" << tc << ": " << count << endl;
    }
    return 0;
}