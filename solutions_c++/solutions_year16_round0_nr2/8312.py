#include <iostream>
#include <cstring>
using namespace std;
const int N = 110;
int main(int argc, const char * argv[]) {
    int t;
    cin>>t;
    for(int c = 1; c <= t; ++c){
        char s[N] = {0};
        memset(s, 0, sizeof(s));
        cin>>s;
        int cnt = 0, len = strlen(s);
        for(int i = 1; i < len; i++){
            if(s[i] != s[i-1])
                cnt++;
        }
        if(s[len-1] == '-')
            cnt++;
        cout<<"Case #"<<c<<": "<<cnt<<endl;
    }
    return 0;
}