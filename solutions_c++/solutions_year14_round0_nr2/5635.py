#include <iostream>
#include <iomanip>

using namespace std;

int main (){
    int T;
    cin >> T;
    cout << fixed << setprecision(7);
    for(int test = 1; test <= T; test++)
    {
        cout << "Case #" << test << ": ";
        double c, f, x;
        cin >> c >> f >> x;
        double ans = x / 2;
        double l = 0, pr = 2;
        for(;;)
        {
            l += c / pr;
            pr += f;
            if (ans > l + x / pr)
                ans = l + x / pr;
            else
                break; 
        }
        cout << ans << endl;
    }
}