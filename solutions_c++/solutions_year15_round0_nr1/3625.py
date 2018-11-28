#include <iostream>
#include <string>

using namespace std;

int main() {
    int T; cin>>T;
    for (int t=1; t<=T; t++) {
        int N; cin>>N;
        string S; cin>>S;
        int tot = S[0]-'0';
        int added = 0;
        for (int i=1; i<S.length(); i++) {
            if (tot<i) added++, tot++;
            tot += S[i]-'0';
        }
        
        cout<<"Case #"<<t<<": "<<added<<endl;
            
    }
    
    return 0;
}
