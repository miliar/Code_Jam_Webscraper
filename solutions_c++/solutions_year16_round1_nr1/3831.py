#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <vector>

using namespace std;

int T;
string S;
vector <char> ans;

int main()
{
    freopen("/Users/yan/Documents/Prep/codeJame/data1Big.txt","r", stdin);
    freopen("/Users/yan/Documents/Prep/codeJame/OUT.txt","w", stdout);
    cin >> T;
    for (int x = 1; x <= T; x++){
        cin >> S;
        char cur = S[0];
        ans.push_back(cur);
        for (int i = 1; i < S.size(); i++){
            //cout << cur << " " << S[i] << endl;
            if (S[i] >= cur){
                //cout << S[i] << endl;
                ans.insert(ans.begin(),S[i]);
                cur = S[i];
            }else{
                ans.push_back(S[i]);
            }
        }

        cout << "Case #" << x << ": ";

        for (int i = 0; i < S.size(); i++){
            cout << ans[i];
        }
        cout << endl;

        ans.clear();

    }
}
