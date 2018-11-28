#include <iostream>
#include <iomanip>

using namespace std;

int main(void) {

    int tasks;
    double c, f, x;
    double no_buy, buy, speed, current, time_elapsed;

    cin >> tasks;
    for(int i = 0; i < tasks; i++) {

        speed = 2.0;
        current = 0.0;
        time_elapsed = 0.0;
        cin >> c >> f >> x;

        if(x < c) {
            cout << "Case #" << i+1 << ": " << fixed << setprecision(7) << (x/speed) << endl;
            continue;
        }

        while(1) {
            time_elapsed += (c/speed);
            current += c;

            buy = x/(speed+f); // if buy
            no_buy = (x-current)/speed; // if not buy
    /*
            cout << "ti = " << time_elapsed << endl;
            cout << "buy = " << buy << endl;
            cout << "no_buy = " << no_buy << endl;
*/
            if(no_buy < buy) {
                cout << "Case #" << i+1 << ": " << fixed << setprecision(7) << (time_elapsed + no_buy) << endl;
                break;
            }
            else {
                current = 0.0;
                speed += f;
            }
        }

    }

    return 0;

}
