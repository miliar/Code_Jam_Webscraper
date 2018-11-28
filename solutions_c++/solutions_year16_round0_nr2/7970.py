#include <iostream>
#include <set>
#include <string>
#include <fstream>
using namespace std;
int main()
{
    ifstream cin("B-large.in");
    ofstream cout("blarge.txt");
    int t,m;
    string s;
    cin>>t;
    for(int k=1;k<=t;k++)
    {
        m=0;
        cin>>s;
        for(int p=s.size()-1;p>=0;p--)
        {
            if(s[p]=='-')
            {
                for(int i=0;i<=p;i++)
                    {
                        if(s[i]=='+') s[i]='-';
                        else s[i]='+';
                    }
                    m++;
            }
        }
        cout<<"Case #"<<k<<": "<<m<<endl;
    }
    return 0;
}
