#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream in("a.txt");
    ofstream out("b.txt");
    int t,w=1;
    in>>t;
    while(t--)
    {
        long long int n,req=0,sum=0,i;
        string s;
        in>>n;
        in>>s;
        //if(s[0]=='0')
        //req+=1;
        for(i=1;i<=n;i++)
        {
            sum=sum+(s[i-1]-'0');
            if(sum>=i) continue;
            else
            {
            req+=i-sum;
            sum+=1;
            }
        }
        out<<"Case #"<<w++<<": "<<req<<endl;
    }
}
