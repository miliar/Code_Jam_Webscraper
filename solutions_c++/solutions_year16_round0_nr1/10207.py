#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    int T; cin >> T;
    for(int t = 1; t <= T; t++){
        int can = 0;
        ll i = 0, x; 
        cin >> x;

        cout << "Case #" << t << ": ";

        if(x == 0) 
            cout << "INSOMNIA\n";
        else{
            while(can != (1<<10)-1){
                ll cp = x * (i + 1LL);
                while(cp) 
                    can |= (1<<(cp%10)), cp /= 10;
                i++;
            }

            cout << x * i << '\n';
        }        
    }
}
