#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int t;
    ifstream in("B-large.in");
    ofstream out("o.txt");
    in>>t;
    string s;
    for(int i=1;i<=t;i++)
    {
        in>>s;
        int o=0;
        for(int j=0;j<s.length();j++)
        {
            if(s[j]=='-'&&s[j-1]=='+')o+=2;
            else if(s[j]=='-'&&s[j-1]!='-')o+=1;

        }

        out<<"Case #"<<i<<": "<<o<<endl;
    }
    return 0;
}
