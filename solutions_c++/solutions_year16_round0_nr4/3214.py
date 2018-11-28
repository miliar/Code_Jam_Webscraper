#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <fstream>
using namespace std;

int main()
{
    ifstream input;
    ofstream output;
    input.open("input.txt");
    output.open("output.txt");
    
    int t;
    input>>t;
    
    for(int i=1 ; i<=t ; i++)
    {
        int c,k,s;
        input>>k>>c>>s;
        output<<"Case #"<<i<<": ";
        for(int j=1 ; j<=k ; j++)
            output<<j<<" ";
        output<<endl;
        
    }
    output.close();
    input.close();
    return 0;
} 
