#include <iostream>
using namespace std;

char s[1000];
int main() {
    int T;
    cin>>T;
    for (int ti=1; ti<=T; ti++) {
        cin>>s;
        char t[1000] = {0};
        int i = 1, j = 500,k=501;
        t[j--] = s[0];
        // cout<<s<<" ";
        while(s[i]) {
            // cout<<s[i]<<" "<<t[j+1]<<"\n";
            if (s[i] >= t[j+1]) {
                t[j] = s[i];
                j--;
            }
            else {
                t[k] = s[i];
                k++;
            }
            i++;
        }
        // s[k]=0;
        // cout<<j<<" "<<k<<endl;
        
        cout<<"Case #"<<ti<<": "<<(t+j+1)<<endl;
    }
    return 0;
}