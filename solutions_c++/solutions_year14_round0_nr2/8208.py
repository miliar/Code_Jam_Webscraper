#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;

int main()
{
    int test, i;
    double cost, time, total, C, X, c, x, F;
    
    ifstream input;
    input.open("Input.txt");
    ofstream output;
    output.open("Output.txt");
    
    input >> test;
    for(i=1;i<=test;i++)
    {
        F = 2.0;
        input >> cost >> time >> total;
    
        C = cost/2;
        X = total/2;
        F+=time;
    
        while(true)
        {
            c = (cost/F)+C;
            x = (total/F)+C;
            if(X<x)
                break;
            else
            {
                C = c;
                X = x;
                F+=time;
            }
        }
        output << "Case #" << i << ": " << setprecision(9) << X << endl;
    }
    return 0;
}
