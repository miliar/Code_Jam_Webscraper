#include <bits/stdc++.h>

using namespace std;

typedef pair<int,int> pii;
typedef long long ll;

#define pb push_back
#define pf push_front
#define mp make_pair
#define sz(a) (int)a.size()
#define i128 __int128
#define INF 0x3f3f3f3f
// LLONG_MIN LLONG_MaX INT_MIN INT_MaX



int main(){
    int n;
    cin >> n;
    for(int i=1; i<=n; i++){
        string s;
        cin >> s;
        int len = s.length();
        int bottom = -1;
        for(int j=len-1; j>=0; j--){
            if(s[j] == '-'){
                bottom = j;
                break;
            }
        }
        int ans = 0;
        while(1){
            if(bottom == -1)
                break;
            if(s[0] == '+'){
                for(int j=0; j<=bottom; j++){
                    if(s[j] == '+')
                        s[j] = '-';
                    else
                        break;
                }
                ans++;
            }
            else{
                int cnt = 0;
                for(int j=0; j<=bottom; j++){
                    if(s[j] == '-')
                        cnt++;
                    else
                        break;
                }
                for(int j=0; j<=bottom; j++){
                    s[j] = (s[j] == '+') ? '-' : '+';
                }
                reverse(s.begin(), s.begin() + bottom + 1);
                bottom -= cnt;
                ans++;
            }
        }
        cout << "Case #" << i << ": " << ans << endl;    
    }
    return 0;
}