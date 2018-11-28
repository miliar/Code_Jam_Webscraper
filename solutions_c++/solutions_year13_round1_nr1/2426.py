#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main ()
{
    ifstream infile ("/Users/diego/Desktop/Google Code Jam/bullseye/data.in");
    ofstream outFile ("/Users/diego/Desktop/Google Code Jam/bullseye/data.out");
    
    int cases;
    long long t;
    long long r;
    
    if (infile.is_open() && outFile.is_open())
    {
        infile >> cases;
        for(int i=0;i<cases;i++)
        {
            //read
            infile >> r;
            infile >> t;
            
            long long n;
            for(n=0;(2*n*n)+(2*r*n)-n<=t;n++);
            cout << n-1 << endl;
            outFile << "Case #" << i+1 << ": " << n-1 << endl;
        }
        
        infile.close();
        outFile.close();
    }
    else cout << "Unable to open file";
    
    return 0;
}