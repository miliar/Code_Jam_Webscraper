#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int t, sh;
string s;
ifstream in ("A.in");
ofstream out ("A.out");
int main()
{
    int i, ans, sik, c=0;
    in>>t;
    while(t--)
    {
        c++;
        sik=0;
        ans=0;
        in>>sh>>s;
        sik=s[0]-48;
        for(i=1; i<=sh; i++)
        {
            if(sik>=i)
            {
                sik+=s[i]-48;
            }
            else
            {
                ans+=i-sik;
                sik=i+s[i]-48;
            }
        }
        out<<"Case #"<<c<<": "<<ans<<"\n";
    }
}
