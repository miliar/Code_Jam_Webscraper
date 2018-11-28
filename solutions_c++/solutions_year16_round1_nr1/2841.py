#include <iostream>
#include <cstdio>
#include <string.h>
using namespace std;

int main()
{
    freopen("in2.in","r",stdin);
    freopen("ans2.txt","w",stdout);
    int t,len=0;
    char str[1001];
    string s;
    cin>>t;
    for(int i = 1 ; i <=t ; ++i)
    {
        len = 1;
        cin>>s;
        str[0] = s[0];
        for(int j = 1 ; j < s.length() ; ++j)
        {
            if(s.at(j) >= str[0])
            {
                for(int p = len-1 ; p>=0; --p)
                {
                    str[p+1]=str[p];
                }
                str[0] = s.at(j);
            }
            else{str[len]=s.at(j);}
            ++len;
        }
        cout<<"Case #"<<i<<": ";
        for(int k = 0 ; k < len ; ++k)
        {
            cout<<str[k];
        }
        cout<<endl;
    }
    return 0;
}
