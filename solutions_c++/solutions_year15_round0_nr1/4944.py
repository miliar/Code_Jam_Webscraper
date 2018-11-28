#include<bits/stdc++.h>
using namespace std;

int n;
string a;

int main(){
    int T_case;
    cin >> T_case;
    for (int tmp_case = 1;tmp_case <= T_case;++tmp_case){
        cin >> n >> a;
        int ans = 0,sum = 0;
        for (int i = 0;i < a.length();++i)
        if ( i <= sum)
        {
            sum += (int)a[i] - 48;
        }
            else
        {
            ans += (i - sum);
            sum += (int)a[i] - 48 + i - sum;
        }
        cout << "Case #" << tmp_case << ": " << ans << endl;
    }
    return 0;
}
