#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream cinn("aa.in",ios::in);
    ofstream coutt("aa1.out",ios::out);
    int t,d=1;
    cinn>>t;
    while(t--)
    {
        int n,i,pa,pr=0,ps;
        cinn>>n;
        string s;
            cinn>>s;
            pa=int(s[0])-48;
        for(i=1;i<=n;i++)
        {
            if(pa>=i)
                pa+=int(s[i])-48;
            else if((int(s[i])-48)!=0)
            {
                ps=i-pa;
                pr+=i-pa;
                pa+=int(s[i])-48+ps;

            }
           // cout<<pa<<" "<<pr<<endl;
        }
        coutt<<"Case #"<<d<<": "<<pr<<"\n";
        d++;
    }
}
