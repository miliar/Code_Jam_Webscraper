#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream in;
    string s;
    int sum,ans,T,max;
    in.open("A-large.in");
    ofstream out;
    out.open("out.txt");
    in>>T;
    for(int t=1; t<=T; t++)
    {
        sum = 0;
        ans = 0;
        in>>max;
        in>>s;
        for(int i=0; i<=max; i++)
        {
            if(sum>=i)
            {
                sum+=(s[i]-'0');
            }
            else
            {
                while(sum<i && s[i]!=0)
                {
                    sum++;
                    ans++;
                }
                sum+=(s[i]-'0');
            }
        }
        out<<"Case #"<<t<<": "<<ans<<endl;
    }
    in.close();
    out.close();
    return 0;
}
