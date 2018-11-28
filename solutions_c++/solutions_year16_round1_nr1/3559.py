#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    long long int t,i,j,k,sum;
    ifstream in("A-large.in");
    ofstream out("out2.in");
    in>>t;
    for(i=1;i<=t;i++)
    {
        string s;
        string str="";
        in>>s;
       // k=-1;
        for(j=0;j<s.length();j++)
        {
            while(1)
            {
                if(k==0)
                    {
                        str+=s[0];
                      //  k++;
                        break;
                    }
                else if(s[j]>=str[0])
                {
                    string s2="";
                    s2+=s[j];
                    s2+=str;
                    str=s2;
                    break;
                }
                else
                {
                    string s2="";
                    s2+=str;
                    s2+=s[j];
                    str=s2;
                    break;
                }

            }
        }
        out<<"Case #"<<i<<": "<<str<<endl;
    }
    return 0;
}
