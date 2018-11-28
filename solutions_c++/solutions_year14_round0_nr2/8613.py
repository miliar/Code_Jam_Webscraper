#include <iostream>

using namespace std;

int main() {
    double rate = 2.0;
    double farmprice = 0.0;
    double farmrate = 0.0;
    double endgame = 0.0;
    double cookies = 0.0;
    double totaltime = 0.0;
    int rounds;
    cout.setf(ios_base::fixed, ios_base::floatfield);
    cout.precision(7);
    cin >> rounds;
    for(int i = 0; i < rounds; i++) {
        cin >> farmprice >> farmrate >> endgame;
	totaltime = 0.0;
	rate = 2.0;
        //decide if you should even consider a farm
        while(cookies != endgame) {
            if((farmprice/rate + endgame/(rate+farmrate)) < (endgame/ rate)) {
                totaltime += farmprice / rate;
                rate += farmrate;
            }
            else {
                totaltime += endgame / rate;
                cookies = endgame;
            }
        }
        cout << "Case #" << i + 1 << ": " << totaltime << "\n";
    }
    return 0;
}
