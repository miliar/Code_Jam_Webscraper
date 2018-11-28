#include <iostream>
using namespace std;

int main() {
    int test_num = 0;
    cin >> test_num;
    
    double C, F, X;
    
    
    for (int i = 1; i <= test_num; i++) {
        double time = 0;
        double addfact = 0;
        double rate = 2.0;
        double potential = 0;
        
        cin >> C >> F >> X;
        //cout << C << F << X << endl;
        
        time = X / rate;
        
        addfact += C / rate;
        
        potential = addfact +  X / (rate + F);
        
        while (time > potential) {
            rate += F;
            addfact += C * 1.0 / rate;
            time = potential;
            potential = addfact + X / (rate + F);
        }
        
        printf("Case #%d: %f\n", i, time);

    }
    
    
}