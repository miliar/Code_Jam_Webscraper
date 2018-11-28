#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

int main()
{
    int t;
    cin>>t;
    string s;
    ofstream myfile;
    myfile.open ("Out.txt");

    for(int i=0;i<t;i++)
    {
        cin>>s;
        int sub = 0;
        int sub2 = 0;
        int counter = 0;
        bool s1 = 1;
        bool s2 = 1;
        for(int j=0;j<s.size();j++)
        {
            if(s[j]=='+'&&s1)
            {
                sub++;
                s1 = 0;
                s2 = 1;
            }
            else if(s[j]=='-'&&s2)
            {
                sub2++;
                counter = sub + sub2;
                s1 = 1;
                s2 = 0;
            }
        }
        myfile<<"Case #"<<i+1<<": "<<counter<< endl;
    }

    myfile.close();

    return 0;
}
