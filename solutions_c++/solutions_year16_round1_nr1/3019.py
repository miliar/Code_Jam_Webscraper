#include <iostream>
#include <fstream>
#include <string>
using namespace std;



int main()
{
    int t;
    ifstream ipf;
    ipf.open("A-large.in");
    ofstream opf;
    opf.open("output.txt");
    ipf >> t;
    ipf.ignore();
    for(int i=1;i<=t;i++)
    {
        string s;
        string res = "";
        getline(ipf,s);
        for(int j =0;j<s.length();j++)
        {
            if (res[0] <= s[j]) res = s[j] + res;
            else res = res + s[j];
        }
        opf << "Case #" << i << ": "<<res<< endl;
    }
}
