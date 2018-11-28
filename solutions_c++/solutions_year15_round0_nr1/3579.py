#include <iostream>
#include <string>

using namespace std;
int main(){

    int t,smax,ans,now;
    string s;
    cin >> t;
    for (int i=0; i<t;i++){
        cin >> smax >> s;
        now = 0;
        ans = 0;
        for (int i=0;i<=smax;i++){
            if (now >= i)
                now += s[i]-'0';
            else {
                int t=i-now;
                now += t + s[i] - '0';
                ans += t;
            }
        }
        cout << "Case #" << i+1 << ": "<< ans << endl;
    }
    return 0;
}

