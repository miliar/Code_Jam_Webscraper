#include <iostream>
#include <string>
#include <cstdio>

using namespace std;
int main(int argc, char **argv) {
    int T;
    cin >> T;
    for(int cn=1;cn<=T;++cn) {
        string S;int K;
        cin >> S >> K;
        int out = 0;
        for(int i=0;i+K<=S.size();++i) {
            if(S[i] == '-') {
                ++out;
                for(int j=0;j<K;++j) {
                    if(S[i+j] == '+') {S[i+j] = '-';}
                    else {S[i+j] = '+';}
                }
            }
        }
        bool ok = true;
        for(int i=0;i<S.size();++i) {
            if(S[i] != '+'){ok = false;}
        }
        if(ok) {
            printf("Case #%d: %d\n", cn, out);
        }
        else {
            printf("Case #%d: IMPOSSIBLE\n", cn);
        }
    }
    return 0;
}
