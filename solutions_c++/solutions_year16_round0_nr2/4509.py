#include<iostream>
#include<string>
using namespace std;

int main()
{
    int i,t,s,c,oe;
    string str;
    cin>>t;
    for(i=1;i<=t;i++)
    {
       cin>>str;
       s=str.length();
       oe=1;
       c=0;
        while(s--)
        {
            if(str[s]=='-'&&oe==1)
            {
            oe=0;
            c++;
            }
            else if(str[s]=='+'&&oe==0)
            {
                c++;
                oe=1;
            }
        }
        cout<<"Case #"<<i<<": "<<c<<endl;
    }
    return 0;
}
