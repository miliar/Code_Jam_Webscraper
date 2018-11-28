#include <iostream>

using namespace std;

int main(int argc, char **argv) {
    
    
    int T, c, i, j;
    double C, F, X;
    double cookies, production, time;
    double farm_time, next_production;
    
    cin >> T;
    
    cout.precision(7);
    
    for ( c = 1; c <= T; ++c ) {
        cin >> C >> F >> X;
        
        time = 0;
        production = 2;
        while( true ) {
            farm_time = C/production + time;
            next_production = production+F;
            if( (X/next_production) + farm_time < (X/production) + time ) {
                production = next_production;
                time = farm_time;
            } else {
                break;
            }
        }
        
        cout << "Case #" << c << ": " << std::fixed << ((X/production) + time ) << endl;
    }
    
    
    return 0;
}