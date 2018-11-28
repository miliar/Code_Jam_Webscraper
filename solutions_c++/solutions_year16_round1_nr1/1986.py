#include<iostream>
#include<fstream>
#include<string>
#include<cmath>
using namespace std;

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("output.out");
    int t;
    fin>>t;
    for(int z=1;z<=t;z++)
    {
        string s,ns;
        fin>>s;
        for(int i=0;i<s.length();i++)
        {
            if(i==0)
            {
                ns.insert(0,1,s[i]);
                continue;
            }
            if(s[i]>=ns[0])
            {
                ns.insert(0,1,s[i]);
            }
            else
                ns.insert(ns.length(),1,s[i]);
        }
        fout<<"Case #"<<z<<": "<<ns<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
