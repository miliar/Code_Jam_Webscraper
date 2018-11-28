#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream input;
    input.open("B-large.in");
    ofstream output;
    output.open("out.txt");

    int t;
    input>>t;

    for(int k=1;k<=t;k++)
    {
        string s;
        input>>s;

        int r=0;
        char prev_c=s[0];

        if(s[0]=='-')
        {
            r=1;
        }
        for(int i=1;i<(int)s.length();i++)
        {
            //cout<<"I="<<i<<"--R="<<r<<"Char = "<<s[i]<<endl;
            if(s[i]=='+')
            {
                prev_c = '+';
                continue;
            }
            if(prev_c == '+')
            {
                r+=2;
                prev_c = s[i];
            }
            //cout<<"I="<<i<<"--R="<<r<<"Char = "<<s[i]<<endl;
        }
        output<<"Case #"<<k<<": "<<r<<endl;
        //cout<<s<<"**Case #"<<k<<": "<<r<<endl;
    }

    return 0;
}
