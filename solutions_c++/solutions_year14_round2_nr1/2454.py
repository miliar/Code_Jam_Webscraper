#include<fstream>
#include<iostream>
#include<string>
#include<cmath>
using namespace std;

string reduce(string s)
{
    int i;
    string ret;
    ret+=s[0];
    for(i=1;s[i];++i)
        if(s[i]!=ret[ret.size()-1])
            ret+=s[i];
    return ret;
}

int main()
{
    ifstream in("x.in");
    ofstream out("output.txt");

    int t,n;
    string s1,s2;
    in>>t;
    for(int x = 1;x<=t;++x)
    {
        in>>n;
        if(n!=2)
            cout<<"N not 2\n";
        in>>s1>>s2;
        string r1 = reduce(s1),r2 = reduce(s2);
        if(r1!=r2)
        {
            out<<"Case #"<<x<<": Fegla Won\n";
        }
        else
        {
            int count = 0;
            for(int i=0,j=0,k=0;r1[i];++i)
            {
                int ctr = 0;
                while(s1[j] == r1[i])
                {
                    ++j;
                    ++ctr;
                }
                while(s2[k] == r1[i])
                {
                    ++k;
                    --ctr;
                }
                count+=abs(ctr);
            }
            out<<"Case #"<<x<<": "<<count<<"\n";
        }
    }
    in.close();
    out.close();
    return 0;
}
