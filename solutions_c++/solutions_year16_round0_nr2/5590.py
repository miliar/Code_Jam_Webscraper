#include<iostream>
#include<fstream>
#include<string>
using namespace std;

long long int pancake(const string& s)
{
    long long int cnt=0;
    char c=s[0];
    for(int i=1;i<s.length();i++)
    {
        if(s[i]==c)
        {
            continue;
        }
        else
        {
            cnt++;
            if(c=='+')
                c='-';
            else c='+';

        }
    }
    if(c=='-')
        cnt++;
    return cnt;
}

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("output.out");
    int t;
    fin>>t;
    for(int k=0;k<t;k++)
    {
        string n;
        fin>>n;
        fout<<"Case #"<<(k+1)<<": "<<pancake(n)<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
