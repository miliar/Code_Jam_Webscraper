#include<bits/stdc++.h>

using namespace std;

int main()
{
    long long int t,l,i,sol;
    string s;
    ifstream ink;
    ofstream out;
    ink.open("input.txt");
    out.open("output.txt");
    ink>>t;
    for(long long int p=1;p<=t;p++)
    {
        out<<"Case #"<<p<<": ";
        ink>>s;
        l=s.length();
        sol=0;
        i=0;
        while(s[i]=='-' && i<l)
        {
            i++;
            sol=1;
        }
        while(i<l)
        {
            while(s[i]=='+' && i<l)
                i++;
            if(s[i]=='-')
            {
                sol=sol+2;
                while(s[i]=='-' && i<l)
                    i++;
            }
        }
        out<<sol<<"\n";
    }
    return 0;
}
