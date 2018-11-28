#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <sstream>
#include <string>
using namespace std;

void megold(istream& in, ostream &out)
{
    string s;
    in>>s;

    // Calculate blocks:
    char last=' ';
    int blocks=0;
    for(int i=0; i<s.size(); i++) {
        if(last!=s[i]) {
            last=s[i];
            blocks++;
        }
    }

    if(s[s.size()-1]=='+')
    blocks--;

    out<<blocks;
}

int main()
{
    ifstream in("B-large.in");
    //ifstream in("test.in");
    ofstream out("pancakes.out");
    int n;
    in>>n;

    //out<<setprecision(12);
    for(int i=1; i<=n; i++)
    {
        out<<"Case #"<<i<<": ";
        megold(in, out);
        out<<endl;
    }
    in.close();
    out.close();
    return 0;
}

