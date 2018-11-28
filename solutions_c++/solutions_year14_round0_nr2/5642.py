#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main (int argc, char* args[]){
    ifstream infile;
    ofstream outfile;
    
    if (argc == 2 && strcmp(args[1], "small") == 0) {
        infile.open("small.in");
        outfile.open("small.out");
    }
    else if (argc == 2 && strcmp(args[1], "large") == 0) {
        infile.open("large.in");
        outfile.open("large.out");
    }
    
    int cases;
    infile >> cases;
    cout << cases << endl ;
    
    //algorithm
    
    double win;
    double cost;
    double boost;
    double result;
    double rate;
    
    // set precission
    outfile << setprecision(numeric_limits<long double>::digits10);
   
    for (int i=0; i<cases; ++i) {
        // read from file
        infile >> cost;
        infile >> boost;
        infile >> win;
        result = 0;
        rate = 2;
        
        // algorithm
        
        while (1){
            if (win/rate <= (cost/rate + win/(rate+boost))){
                result += win/rate;
                break;
            }
            else {
                result += cost/rate;
                rate += boost;
            }
        }
        
        outfile << "Case #" << i+1 << ": " << result << endl;

    }
    
    infile.close();
    outfile.close();
    
    return 0;
}
