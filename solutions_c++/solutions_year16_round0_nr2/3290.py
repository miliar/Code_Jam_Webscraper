#include<iostream>
#include<cstring>
#include<string>
using namespace std;
int main()
{
    int t,r;
    cin>>t;
    r=1;
    for(; r<=t; r++)
    {
        string s;
        cin>>s;
        int l=s.length(),m=0,j,flag=0,c=0;

        for(j=0; j<l-1; j++)
        {
            if(s[j]=='-'&&s[j+1]=='+')
                m++;
        }
        if(s[l-1]=='-')
            m++;
        if(s[0]=='-')
          c=2*m-1;
        else
            c=2*m;
        cout<<"Case #"<<r<<": "<<c<<"\n";
    }
    return 0;
}
