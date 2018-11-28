#include <iostream>
#include <cstdio>

using namespace std;

int T,smax,n,cur,ans;
string in;

int main()
{
    freopen("in1l.txt","r",stdin);
    freopen("out1l.txt","w",stdout);
    cin >> T;
    for (int j = 1; j <= T; j++){
        cur = 0; ans = 0;
        cin >> smax >> in;
        for (int i = 0; i <= smax; i++){
            n = in[i]-'0';
            if (cur < i){
                ans += i-cur;
                cur = i;
            }
            cur += n;
        }
        cout << "Case #" << j << ": " << ans << endl;
    }
    return 0;
}

