#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t,l,i,ans;
    string s;
    ifstream in;
    ofstream out;
    in.open("input.txt");
    out.open("output.txt");
    in>>t;
    for(int z=1;z<=t;z++)
    {
        out<<"Case #"<<z<<": ";
        in>>s;
        l=s.length();
        //while(find(s.begin(),s.end(),'-')!=s.end())
            ans=0;
            i=0;
                while(s[i]=='-' && i<l)
                {
                    i++;
                    ans=1;
                }
                while(i<l)
                {
                while(s[i]=='+' && i<l)
                    i++;
                if(s[i]=='-')
                {
                    ans+=2;
                    while(s[i]=='-' && i<l)
                        i++;
                }
                }
        out<<ans<<endl;
    }
    return 0;
}
