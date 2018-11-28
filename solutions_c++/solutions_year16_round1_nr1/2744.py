#include <bits/stdc++.h>

using namespace std;

const int maxN = 1005;

int main(){
  freopen("A-large.in","r",stdin);
    freopen("on.c","w",stdout);

    int tc;
    cin >> tc;
    for(int t = 1; t <= tc; ++t){
        string s;
        cin >> s;
        int n = s.size();

        string answer ;
        for(int i = 0; i < n; ++i){
            if(answer.size() == 0 || s[i] >= answer[0]){
                answer = s[i] + answer;
            }else{
                answer.push_back(s[i]);
            }
        }
        printf("Case #%d: ",t);
        cout << answer << endl;
    }

    return 0;
}
