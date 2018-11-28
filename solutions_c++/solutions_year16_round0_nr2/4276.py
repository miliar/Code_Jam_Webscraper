#include <iostream>  
#include <fstream>
#include <string.h>
#include <stdio.h>
using namespace std;
int main()
{
    ofstream myfile;
    ifstream inputfile("input.txt");
    int t;
    inputfile >> t;
    myfile.open("example.txt");
    string s;
    getline(inputfile,s);
    for (int i = 1; i <= t; ++i)
    {
        char c;
        getline(inputfile,s);
        int count=0;
        c=s[0];
        for(int i=1;i<s.size();i++)
        {
            if(c!=s[i])
            {
                count++;
                c=s[i];
            }
        }
        if(c=='-')
            count++;
        myfile << "Case #" << i << ": " << count << endl;
    }
    myfile.close();
    inputfile.close();
}