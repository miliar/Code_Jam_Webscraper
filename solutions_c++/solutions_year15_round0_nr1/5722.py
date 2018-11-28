#include <stdlib.h>
#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <iterator>
#include <string>

using namespace std;

#define INPUT "A-large.in"
#define OUTPUT "A-large.out"

int main()
{
    int  T;
    string s;
    ifstream in;
    in.open(INPUT, ios::in);
    ofstream out;
    out.open(OUTPUT, ios::out);
    getline(in, s);
    T= atoi(s.c_str());
    for(int t=1; t <=T; t++)
    {
        getline(in, s);
        //int smax = atoi(s.substr(0, s.find_first_of(" ")).c_str());
        s = s.substr(s.find_first_of(" ")+1, s.size()-1);
        int N=0, standing=s[0]-'0';
        for(int i=1; i< s.size(); i++)
        {
            if(standing<i)
            {
                N+=(i-standing);
                standing +=(i-standing);
            }
            standing+= s[i]-'0';
        }

        out <<"Case #"<<t<<": "<<N<<endl;
    }
    in.close();
    out.close();
}




