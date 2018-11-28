#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("out.txt", "w", stdout);
    int t; cin >> t;
    int ta = t;
    while(t--){
        int sm; cin >> sm;
        int sum = 0;
        int re = 0;
        string s; cin >> s;
        for(int i = 0; i <= sm; i++){
            int tmp = s[i]-'0';
            int lis = 0;
            if(sum<i){
                re+=i-sum;
                lis = i-sum;
            }
            sum+=lis+tmp;
        }
        cout << "Case #" << ta-t << ": " << re << endl;
    }
    return 0;
}
