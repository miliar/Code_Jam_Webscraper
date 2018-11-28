#include <iostream>
#include <string>
using namespace std;

int main() {
    int t;
    cin>>t;
    int j=0;
    while(t--) {
        j++;
        string s;
        cin>>s;
        int count=0;
        int len = s.length();
        for (int i=0; i<len-1; i++) {
            if(s[i] != s[i+1])
                count++;
        }
        if(s[len-1]=='-')
            count++;

        cout<<"Case #"<<j<<": "<<count<<endl;
    }
    return 0;
}
