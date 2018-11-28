#include <iostream>
#include <sstream>
#include <map>
#include <vector>
#include <list>
#include <fstream>
#include <algorithm>;
#include <iomanip>   

using namespace std;
typedef unsigned int uint;


void solve(istream& is, uint index)
{
    double c, f, x;
    is >> c; is >> f; is >> x;
    
    double t = 0.0;
    double rate = 2.0;
    double best_time = x / rate;
    
    bool stop = false;
    while (stop == false) {
        t += c / rate;
        rate += f;
        double new_time = x / rate + t;
        
        if (new_time < best_time) {
            best_time = new_time;
        } else {
            stop = true;
            cout << "Case #" << index << ": " << fixed << setprecision (7) << best_time << endl;
        }
    }
}

void oef(istream& is)
{
    uint n;
    is >> n;
    for(uint i = 0;i < n; i++)
        solve(is, i+1);
}

#define EIGENTEST 1

int main()
{
    ifstream myfile ("/home/thomas/Downloads/B-large.in");
    
    if (myfile.is_open())
    {
        oef(myfile);
        
        myfile.close();
    }
    
    return 0;
}

