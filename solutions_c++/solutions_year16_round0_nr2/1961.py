#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

int main() {
    int T;
    cin>>T;
    for (int i=1;i<=T;i++) {
        int ans=0;
        string s;
        cin>>s;
        int j=s.size()-1;
        while (j>=0) {
            while (j>=0 && s[j]=='+') j--;
            if (j>=0) {
                if (s[0]=='+') {
                    int k=j;
                    while (k>=0 && s[k]=='-') k--;    
                    reverse(s.begin(),s.begin()+k+1);
                    for (int l=0;l<=k;l++)
                        s[l] = (s[l]=='+')? '-':'+';
                    ans++;
                }
                reverse(s.begin(),s.begin()+j+1);
                for (int l=0;l<=j;l++)
                    s[l] = (s[l]=='+')? '-':'+';
                ans++; 
            }           
            //cout<<s<<endl;
        }
        cout << "Case #" << i << ": " << ans << endl;
    }
    return 0;
}