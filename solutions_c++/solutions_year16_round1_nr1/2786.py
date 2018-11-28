#include <iostream>

using namespace std;



int main()
{
    std::ios::sync_with_stdio(false);
    int t,T;
    cin >> T;
    for (t=0; t<T; t++)
    {
        string s,ans="";
        cin >> s;
        for (int i=0; i<s.size(); i++) {
            if (i==0) {
                ans += s[i];
            }
            else{
                if (s[i] >= ans[0]) {
                    
                    ans = s.substr(i,1)+ans;
                }
                else{
                    ans = ans + s.substr(i,1);
                }
            }
        }
        cout <<"Case #"<<t+1<<": "<< ans <<endl;
    }
    return 0;
}

