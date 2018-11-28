#include <iostream>
#include <stdio.h>
#include <iomanip>

using namespace std;

double c, f, x;
double c0, f0, x0;
double min;

int main() {
    freopen("data.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int N;
    cin>>N;
    int n = 0;
    while(N--) {
        cin>>c>>f>>x;
        double simTime = 0, totalTime1 = 0, totalTime2 = 0, s = 2.0;
        do {
            totalTime1 = simTime + x/s;
            totalTime2 = simTime + c/s + x/(s+f);
            simTime += c/s; s += f;
//            cout<<totalTime1<<" "<<totalTime2;
        } while(totalTime1 > totalTime2);
        n++;
        cout<<"Case #"<<n<<": "<<fixed<<setprecision(7)<<totalTime1<<endl;
    }
    return 0;
}
