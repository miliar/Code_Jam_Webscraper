#include <iostream>
#include <iomanip>

using namespace std;

int main(int argc, const char * argv[])
{
    freopen("/Users/sancruise7/Developer/CodeJam/input.txt","r",stdin);
    freopen("/Users/sancruise7/Developer/CodeJam/output.txt","w",stdout);
    int T,i;
    double cost,step,win;
    double start = 2.0;
    double time,currentCookie;
    cin >> T;
    //cout << T << endl;
    for (i = 0; i < T; i++) {
        cin >> cost >> step >> win;
        //cout << fixed << setprecision(5) << cost << " " << step << " " << win << endl;
        time = 0.0;
        currentCookie = start;
        while ((win/currentCookie) > (cost/currentCookie + win/(currentCookie + step))) {
            time += cost/currentCookie;
            currentCookie += step;
        }
        time += win/currentCookie;
        cout << "Case #" << i+1 << ": ";
        cout << fixed << setprecision(7) << time << endl;
    }
    return 0;
}
