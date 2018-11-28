#include <iostream>
#include <iomanip>
#include <algorithm>

using namespace std;

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cout << fixed << setprecision(10);
    int t;
    cin >> t;
    t++;
    for ( int test = 1; test < t; test++ ){
        cout << "Case #" << test << ": ";
        int n;
        cin >> n;
        long double naomi[2000], ken[2000];
        for ( int i = 0; i < n; i++ )
            cin >> naomi[i];
        for ( int i = 0; i < n; i++ )
            cin >> ken[i];
        sort(ken, ken + n);
        sort(naomi, naomi + n);
        
        int l_naomi = 0;
        int l_ken = 0;
        int ans = 0;
        while ( l_naomi < n ){
            if ( naomi[l_naomi] < ken[l_ken] ){
                l_naomi++;
                ans++;
            }else{
                l_naomi++;
                l_ken++;
            }
        }
        cout << n - ans << ' ';
        
        l_naomi = 0;
        l_ken = 0;
        ans = 0;
        while ( l_ken < n ){
            if ( naomi[l_naomi] > ken[l_ken] ){
                l_ken++;
                ans++;
            }else{
                l_naomi++;
                l_ken++;
            }
        }
        
        cout << ans << endl;
    }
    return 0;
} 
