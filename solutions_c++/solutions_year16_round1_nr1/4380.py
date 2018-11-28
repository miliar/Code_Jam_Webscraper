#include<bits/stdc++.h>
using namespace std;
int main() {

    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin>>t;

    string str;
    string res;
    for(int i=0; i<t; i++) {
        cin>>str;
        for(int j=0; j<str.size(); j++) {
            if(!j)
                res.push_back(str[j]);
            else {
                if(str[j]<res[0]) {
                    res.push_back(str[j]);
                } else {
                    res.insert(0,1,str[j]);
                }
            }
        }

        cout << "Case #" << i+1 <<": " << res << endl;
        res.clear();
    }
    return 0;
}
