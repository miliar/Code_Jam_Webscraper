#include <iostream>

using namespace std;

int main () {
        int test, i, ans = 0, k;
        string s;
        cin >>test;
        k = 1;
        while(test--){
                cin>>s;
                for (i=0; i<(s.length()-1); i++) {
                        if(s[i] != s[i+1]) {
                                ans++;
                        }
                }
                if (s[s.length()-1] == '-') {
                        ans++;
                }
                cout<<"Case #"<<k<<":"<<" "<<ans<<"\n";
                k++;
                ans = 0;
        }
        return 0;
}