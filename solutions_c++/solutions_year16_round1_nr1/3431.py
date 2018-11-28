#include <iostream>
#include <fstream>

using namespace std;

ifstream fin;
ofstream fout;

int main()
{
    fin.open("A-large.in");
    fout.open("test.out");
    string s,ss;char c;int n;
    fin>>n;
    for(int w=0;w<n;w++)
    {
        fin>>s;
        ss=s[0];
        c=s[0];
        fout<<"Case #"<<w+1<<": ";
        for(int i=1;i<s.length();i++)
        {
            if(s[i]>=c)
            {
                ss=s[i]+ss;
                c=s[i];
            }
            else
            {
                ss+=s[i];
            }
        }
        fout << ss << endl;


    }

    return 0;
}
