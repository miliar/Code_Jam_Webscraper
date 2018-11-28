#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    cin >> T;
    int n;
    string s;
    int standing,add;
    for(int t=0; t<T; t++){
        cin >> n >> s;
        standing=0, add=0;
        for(int i=0; i<(int)s.length(); i++){
            if(s[i]=='0')
                continue;
            else if(standing >= i)
                standing += (int)(s[i]-'0');
            else{
                add+= (i-standing);
                standing = i + (int)(s[i]-'0');
            }
        }
        cout << "Case #" << t+1 << ": " << add << endl;
    }
    return 0;
}
