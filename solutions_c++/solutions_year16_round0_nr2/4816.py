#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    ifstream fbe("B-large.in");
    ofstream fki("ki-l.txt");
    int T;
    fbe>>T;
    for (int i=0; i<T; i++)
    {
        string s;
        fbe>>s;
        string ujs="";
        char elozo='+';
        for (int k=s.length()-1; k>=0; k--)
        {
            if (s[k]!=elozo){elozo=s[k]; ujs+=s.substr(k,1);}
        }
        fki<<"Case #"<<i+1<<": "<<ujs.length()<<endl;
    }

    fbe.close();
    fki.close();
    return 0;
}
