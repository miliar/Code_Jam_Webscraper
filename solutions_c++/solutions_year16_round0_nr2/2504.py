#include<iostream>
#include<fstream>
#include <string>

using namespace std;

int main ()
{
    ifstream ifile("B-large.in");
    ofstream ofile;
    ofile.open("B-large.out");
    long long t, cases = 0, count1 = 0;
    string s;
    ifile>>t;
    char c;
    while(t--)
    {
        ifile>>s;
        count1 = 0;
        c = s[0];
        int n = s.length();
        for(int i = 0; i < n; ++i)
        {
            while(i < n && s[i] != '-')
            {
                i++;
            }
            if(i < n && s[i] == '-')
            {
                ++count1;
                if(c == '+')
                    c = '-';
                else
                    c = '+';
            }
            while(i < n && s[i] != '+')
            {
                i++;
            }
            if(i < n && s[i] == '+')
            {
                if(c == '-')
                    ++count1;
                c = '+';
            }
        }
        if(c == '-')
            ++count1;
        //cout<<"Case #"<< ++cases<<": "<< count1<<endl;
        ofile<<"Case #"<<++cases<<": "<<count1<<endl;
        s.empty();
    }
}

