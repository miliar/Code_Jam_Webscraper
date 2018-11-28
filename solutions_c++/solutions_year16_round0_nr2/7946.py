#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
    freopen("in2.in","r",stdin);
    freopen("ans2.txt","w",stdout);
    int t,total;
    char c;
    string s;
    cin>>t;
    for(int i = 1 ; i <= t ; ++i)
    {
        total = 0;
        cin>>s;
        if(s.length() == 1){if(s.at(0)=='-'){cout<<"Case #"<<i<<": 1\n";}else{cout<<"Case #"<<i<<": 0\n";}}
        else{
           c = s.at(0);
           for(int j = 1 ; j<s.length() ; ++j)
           {
               if(s.at(j) != c){++total;}
               c = s.at(j);
           }
           if(s.at(s.length()-1) == '-'){++total;}
           cout<<"Case #"<<i<<": "<<total<<endl;
        }
    }
    return 0;
}
