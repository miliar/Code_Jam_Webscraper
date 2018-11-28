#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int main()
{
    string s;
    char ch;
    int no_of_chng,t;
    ifstream fin("B-large.in");
    ofstream fout("out.txt");
    fin>>t;
    for(int j=0;j<t;j++)
    {
        fin>>s;
        ch=s[0];
        no_of_chng=1;
        for(int i=1;i<s.length();i++)
        {
            if(s[i]!=ch)
            {
                ch=s[i];
                no_of_chng++;
            }
        }
        if(ch=='-')
            fout<<"Case #"<<j+1<<": "<<no_of_chng<<"\n";
        else
            fout<<"Case #"<<j+1<<": "<<no_of_chng-1<<"\n";
        cout<<no_of_chng;
    }
    return 0;
}
