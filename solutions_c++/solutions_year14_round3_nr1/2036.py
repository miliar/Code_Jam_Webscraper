#include <iostream>
#include <algorithm>
#include <cmath>
#include <fstream>
#include <string>
#include <sstream>
#include <iomanip>
#include <map>
using namespace std;
typedef long long int LL;
//#define fin cin
//#define fout cout
int main()
{
    ios_base::sync_with_stdio(0);
    ifstream fin("A-small-attempt2 (1).in");
    ofstream fout("A-small-attempt2 (1).out");
    int t;
    fin>>t;
    for(int k=1;k<=t;k++)
    {
        string s;
        fin>>s;
        for(int i=0;i<s.size();++i)
            if(s[i]=='/')
            {
                s[i]=' ';
                break;
            }
        stringstream ss(s);
        int a, b, ans=0;
        ss>>a>>b;
        //fout<<a<<" "<<b<<endl;
        int fans;
        bool chk2=true;
        if(b%2!=0)
        {
            fout<<"Case #"<<k<<": impossible"<<endl;
        }
        else
        {
            bool chk=true;
            while(b%2==0)
            {
                b/=2;
                ans++;
                if(a==b)
                {
                    chk=false;
                    if(chk2)
                        fans=ans;
                    break;
                }
                else if(a>b)
                {
                    if(chk2)
                        fans=ans;
                    chk2=false;
                    a-=b;
                }
            }
            if(chk)fout<<"Case #"<<k<<": impossible"<<endl;
            else fout<<"Case #"<<k<<": "<<fans<<endl;
        }
    }
    return 0;
}
