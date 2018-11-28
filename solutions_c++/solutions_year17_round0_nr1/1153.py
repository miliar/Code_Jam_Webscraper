#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    int t,k;
    cin>>t;
    for(int tt=1;tt<=t;tt++) {
        string p;
        cin>>p>>k;
        cout << "Case #"<<tt<<": ";
        int l=p.length(), c=0;
        for(int i=0;i<l;i++) {
            if(p[i]=='-' and i+k<=l) {
                c++;
                for(int j=i;j<i+k;j++) {
                    if(p[j]=='+') p[j]='-';
                    else p[j]='+';
                }
            }
        }
        int i=0;
        for(i=0;i<l;i++) if(p[i]=='-') break;
        if(i==l) cout << c << "\n";
        else cout << "IMPOSSIBLE\n";
    }
    return 0;
}
