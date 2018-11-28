#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

int main(){
    int t;
    std::cout << std::setprecision(7) << std::fixed;
    cin >> t;
    for(int k = 0; k < t; k++){
        double c, f, x;
        cin >> c >>f>>x;
        double minsum=0, next=0, current=0;
        for(int i = 0;;i++){
            current=x/(2+f*i);
            next = c/(2+f*i)+x/(2+f*(i+1));
            if(current < next){
                minsum = minsum + current;
                break;
            }
            else minsum = minsum + c/(2+f*i);
        }
        cout << "Case #" << k+1 <<": " << minsum << endl;
    }
}
