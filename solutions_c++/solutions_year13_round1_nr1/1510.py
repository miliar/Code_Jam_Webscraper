#include <algorithm>
#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <fstream>
#include <cctype>
#include <math.h>
#include <cstdlib>

using namespace std;

typedef vector<int>::iterator iter;
typedef vector<int>::reverse_iterator riter;
typedef vector<string>::iterator str_iter;
typedef unsigned long long ull;
typedef long long ll;

int main()
{
    ifstream infile("A-small-attempt0.in");
    ofstream outfile("out.txt");
    int cases;
    string line;
    getline(infile, line);
    istringstream str(line);
    str >> cases;
    
    for (int j = 0; j != cases; ++j) {
        getline(infile, line);
        istringstream first(line);
        ll r, t;
        first >> r >> t;
        
        ll count = 0;     
        while (t > 0) {
            t -= 2*r + 1;
            r += 2;
            ++count;
        }
        if (t < 0) --count;
        
        
        outfile << "Case #" << j+1 << ": " << count << endl;
    }
   
    return 0;
}