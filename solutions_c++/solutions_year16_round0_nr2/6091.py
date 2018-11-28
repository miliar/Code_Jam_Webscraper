#include <iostream>
#include <string>

using namespace std;

int main() {
    string str;
    int T, n, i, cnt, pi;

    cin>>T;

    int c=1;
    for (; c<=T; ++c) {
        cin>>str;

        i=str.size()-1;
        while (i >= 0 && str[i] == '+') {
            --i;
        }
        
        cnt=0;
        if (i >= 0) {
            ++cnt;
            pi=i;
            
            for (; i>=0;--i) {
                if (str[pi] != str[i]) {
                    ++cnt;
                    pi=i;
                }
            }
        }
        
        cout<<"Case #"<<c<<": "<<cnt<<"\n";
        
    }

    return 0;
}

