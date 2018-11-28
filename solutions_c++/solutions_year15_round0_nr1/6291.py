#include<fstream>
#include<iostream>
#include<string>
using namespace std;
int main ()
{
    string s;
    int T,n;
    ifstream in("A-large.in");
    ofstream out("output.txt");
    in>>T;
    for(int i=1;i<=T;i++)
    {
        in>>n>>s;
        int k=0,sum=0;
        for(int i=0;i<=n;i++)
        {
            if(s[i]!='0')
            {
                if(i>sum)
                {
                    k+=(i-sum);
                    sum+=(i-sum);
                }
                sum+=s[i]-'0';
            }
        }
        out<<"Case #"<<i<<": "<<k<<"\n";
    }
}
