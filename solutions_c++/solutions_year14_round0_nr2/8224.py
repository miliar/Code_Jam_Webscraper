#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <math.h>
#include <cmath>

using namespace std;
bool compare(double x, double y)
{
    double absTol = 0.0000001;
    if (abs(x - y) <= absTol * max(double(1), max(abs(x), abs(y))))
    {
        // means x== y 
        return false;
    }
    else if ( x > y)
    {
        // 
        return true;
    }
}

int process_case(vector<string> s, int out)
{
    double c;
    double f;
    double x;
    double p =2;
    double t = 0;
    string input_1 = s[out];
    istringstream(input_1) >> c >> f >> x;
    std::cout << std::fixed;
    std::cout << std::setprecision(7);
    
    
    while ( compare( ((x-c)*f) - (c*p), 0))
    {
        t = t + (c/p);
        p = p+f;
    }
    t = t+ (x/p);
    cout<<"Case #"<<out<<": "<<t<<endl;
    return 0;
    
}
int main(int argc, char *argv[]) 
{
    
    string line;
    vector <string> s;
    ifstream myfile;
    myfile.open ("input.txt");
    if (myfile.is_open())
    {
        while (true) 
        {
            getline(myfile, line);
        //  getline(cin, line);
                
            if (line.empty())
            {
                    break;
            }
            else
            {
                s.push_back(line);
                }
        }
    }
    else
    {
        cout<<"siva unable to open the file"<<endl;
    }
    
    int num_case = stoi(s[0]);
    for (int i =1 ; i<= num_case; i++)
    {
        process_case(s,i);
    }
    
   return 0;
}
