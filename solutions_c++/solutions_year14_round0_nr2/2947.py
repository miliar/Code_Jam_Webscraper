#include<iostream>
#include<vector>
#include<climits>

using namespace std;


//Cookie Clicker Alpha
int main( int argc, const char* argv[] ) {
    cout.setf( ios::fixed, ios::floatfield );
    cout.precision( 7 );

    int t;
    cin >> t;
    
    for( int i = 1; i <= t; i++ ) {
        double c, f, x;
        cin >> c >> f >> x;

        int j = 0;
        double farmCost = 0;
        double totalCost = x / 2;
        double oldTotalCost = 1e7;

        while( oldTotalCost > totalCost ) {
            oldTotalCost = totalCost;
            farmCost += c / (2 + j*f);
            j++;
            totalCost = farmCost + x / (2 + j*f);
        }

        cout << "Case #" << i << ": " << oldTotalCost << endl;
    }

    return 0;
}
