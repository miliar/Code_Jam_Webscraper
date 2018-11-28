#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main() {
    double currentSpeed = 2,cases;
    double c,f,x,time =0.0;
    cout <<fixed;
    cout << setprecision(7);
    cin >> cases;
    for(int icase = 1; icase <=cases;icase++){
        currentSpeed=2;
        time = 0;
        cin >> c;
        cin >> f;
        cin >> x;
        cout << "C: "<<c << " F: "<<f<<" X: "<<x<<endl;
        while(1){
            if((x/currentSpeed) < ((c/currentSpeed)+(x/(currentSpeed+f)))){
                time += (double) abs(x)/abs(currentSpeed);
                    break;
            }else{
                time += (double)abs(c)/abs(currentSpeed);
                currentSpeed += f;
                cout << "Time: "<< time<<endl;
            }
        }
        cout << "Case #"<<icase<<":"<<time << endl;
    }
    return 0;
}
