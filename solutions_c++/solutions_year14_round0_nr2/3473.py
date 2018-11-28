#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cout << fixed << setprecision(7);
    int t;
    cin >> t;
    t++;
    long double c, f, x;
    for ( int test = 1; test < t; test++ ){
        cin >> c >> f >> x;
        long double ans = 0;
        long double speed = 2;
        while (true){
            long double tnow = x / speed;
            long double tnext = x / (speed + f) + c / speed;
            if (tnow <= tnext){
                ans += tnow;
                break;
            }else{
                ans += c / speed;
                speed += f;
            }
        }
        cout << "Case #" << test << ": " << ans << endl;
    }
    return 0;
}
