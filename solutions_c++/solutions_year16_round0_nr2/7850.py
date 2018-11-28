#include<bits/stdc++.h>
using namespace std;

int main()
{
    ifstream in("B-large.in");
    ofstream out("pancakesout_large.txt");
    int t;
    in>>t;
    for(int j=1; j<=t; ++j)
    {
        string s;
        in>>s;
        int c=0;
        int l=s.size();
        for(int i=1;i<l; ++i)
        {
            if(s[i-1]!=s[i])
                c++;
        }
        if(s[l-1]=='+')
            out<<"Case #"<<j<<": "<<c<<endl;
        else
            out<<"Case #"<<j<<": "<<c+1<<endl;
    }
    return 0;
}
