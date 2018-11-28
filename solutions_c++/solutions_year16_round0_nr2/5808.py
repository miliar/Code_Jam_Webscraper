#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int main()
{
    long long int t,i,j,k,n;
    ifstream in("B-large.in");
    ofstream out("out1.in");
    in>>t;
    for(i=1;i<=t;i++)
    {
        string s;
        in>>s;
        long long int sum=0;
        for(j=s.length()-1;j>=0;)
        {
            if(s[j]=='-' && s[0]=='+')
            {
               k=0;
            while(k<j && s[k]=='+')
            {
                s[k]='-';
                k++;
            }
            //cout<<s<<endl;
            sum++;
            }
            else if(s[j]=='-')
            {
                string str="";
                k=j;
                while(k>=0)
                {
                    if(s[k]=='-')
                        s[k]='+';
                    else
                        s[k]='-';
                    str+=s[k];
                    k--;
                }
                string s2="";
                if(j+1<=s.length()-1)
                s2=s.substr(j+1,s.length()-j-1);

                s=str+s2;
               // cout<<s<<endl;
                sum++;
                j--;
            }
            else
                j--;
        }
        out<<"Case #"<<i<<": "<<sum<<endl;

    }
}
