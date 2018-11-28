#include <iostream>
#include <iomanip>
#include <math.h>
using namespace std;

int main(){
    long long int T, r, L;
    ifstream ifile;
    ofstream ofile;
    ifile.open("AS.in");
    ofile.open("AS.out");
    cin >> T;
    for (int i=1;i<=T;i++){
        cin >> r >> L;
        cout << setprecision(0) << fixed << "Case #" << i << ": " << floor(((1-2*r)+sqrt((2*r-1)*(2*r-1)+8*L))/4) << endl;
    }
}
