#include <iostream>
#include <string>
using namespace std;


int main() {
    int T; cin>>T;
    for (int t=1; t<=T; t++) {
        string s; cin>>s;
        s+='+';
        int cnt = 0;
        for (int i=0; i<int(s.size())-1; i++)
            cnt += (s[i] != s[i+1]);
        cout<<"Case #"<<t<<": "<<cnt<<endl;
    }
    return 0;
}
