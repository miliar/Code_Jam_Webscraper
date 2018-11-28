#include <iostream>
#include <vector>
#include <string>
#include <map>

#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>

using namespace std;
string word;


int main() {
//cout<<"here"<<endl;
    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A-small-output0.text", "w",stdout);
    freopen("A-large.in", "r", stdin);
    freopen("A-large-output.txt", "w", stdout);

    int T;
    cin>>T;
    for(int tc = 1; tc <= T; tc++) {
        cout<<"Case #"<<tc<<": " ;
        cin>>word;
        string res = "";
        res += word[0];
        for(int i = 1; i < word.size(); i++) {
            string res1=res + word[i];
            
            string res2 = "";
            res2 = res2 + word[i];
            res2 += res;
            
            if(res1 > res2) {
                res = res1;
            }else res = res2;
        }
        
        cout<<res<<endl;
    }

    return 0;
}
