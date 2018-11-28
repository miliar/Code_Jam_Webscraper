#include <iostream>
#include <string>
using namespace std;


int main() {
    int t, t_case;
    
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);

    cin >> t;
    for(t_case = 1; t_case <= t; ++t_case) {
        
        int i, x, y;
        cin >> x >> y;
        string ans;

        string ye = "SN", xe = "WE";
        
        if(y < 0)
            ye = "NS",
            y *= -1;
        if(x < 0) 
            xe = "EW",
            x *= -1;

        for(i = 1; i <= x; ++i)
            ans += xe;

        for(i = 1; i <= y; ++i)
            ans += ye;

        cout << "Case #" << t_case << ": " << ans << "\n";
    }  
    
    return 0;
}
