#include <iostream>
#include <fstream>

using namespace std;

ifstream fin;
ofstream fout;

int main()
{
    fin.open("B-large.in");
    fout.open("test1.out");
    int numm,n;char x;
    string s;
    fin>>n;
    for(int b=0;b<n;b++)
    {
        fin>>s;
        fout<<"Case #"<<b+1<<": ";
        x=s[0];
        numm=0;
        for(int i=0;i<s.length();i++)
        {
            if(s[i]!=x)
            {
                ++numm;
                x=s[i];
            }
        }
        if(s[s.length()-1]=='-')
        {
            ++numm;
        }
        fout<<numm<<endl;
    }

    return 0;
}
