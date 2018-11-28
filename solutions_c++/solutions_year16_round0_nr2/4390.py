#include <iostream>
#include <sstream>

using namespace std;

int main(){
    int tc;
    cin >> tc;
    for(int c = 1; c <= tc; c++){
        string ch;
        cin >> ch;
        long long ans = 0;
        while(1){
            bool done = true;
            for(int i = ch.size(); i >= 0; i--){
                if(ch[i] == '-'){
                    for(int j = i; j >= 0; j--)
                        ch[j] = ch[j] == '-' ? '+':'-';
                    done = false;
                    break;
                }
            }
            if(done) break;
            ans ++;
        }
        printf("Case #%d: %lld\n", c, ans);
    }
    return 0;
}
