#include <iostream>
#include <set>
#include <cstdio>
#include <string>
#include <sstream>
#define add push_back;
using namespace std;
int main()
{

    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int t=0;
    int i=0,j=0,h=0;
    cin>>t;
    for(h=0;h<t;h++)
    {
        string s="",temp="";
        cin>>s;
        for(i=0;i<s.size();i++)
        {
            if(i==0)
            {
                temp+=s[i];
            }
            else
            {
                if(s[i]>=temp[0])
                {
                    temp=s[i]+temp;
                }
                else
                {
                    temp+=s[i];
                }
            }
        }
        cout<<"Case #"<<(h+1)<<": "<<temp<<"\n";
    }
      return 0;
}
