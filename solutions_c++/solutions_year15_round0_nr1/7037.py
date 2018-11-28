#include<bits/stdc++.h>
using namespace std;
#define len(val) static_cast<int>(val.size())
#define rep(i, n) for(int i=0; i<(n); i++)
typedef long long ll;
typedef pair<int, int> P;


int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);

    int N;
    cin >> N;
    rep(n, N){
        int M;
        string s;
        cin >> M >> s;
        int res = 0;
        int now = s[0]-'0';
        for(int i=1; i<len(s); i++){
            if(now >= i){
                now += s[i]-'0';
            }else{
                res += i-now;
                now = i;
                now += s[i]-'0';
            }
        }
        cout << "Case #" << n+1 << ": " << res << endl;
    }
}
