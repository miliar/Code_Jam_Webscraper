#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,p;
    ifstream IF;
    ofstream OF;
    IF.open("input.txt");
    OF.open("output.txt");
    IF>>t;
    for(p=1;p<=t;p++)
    {
        long long int k,i,j,ln=0,lp=-1,l;
        string s;
        IF>>s;
        l=s.length();
        for(i=0;i<l;i++)
        {
            if(s[i]=='-')
            {
                if(i==0)
                    ln=1;
                else
                {
                    if(s[i-1]!=s[i])
                    {
                        ln+=2;
                    }
                }
            }
        }
        OF<<"Case #"<<p<<": "<<ln<<endl;
    }
    IF.close();
    OF.close();
    return 0;
}

