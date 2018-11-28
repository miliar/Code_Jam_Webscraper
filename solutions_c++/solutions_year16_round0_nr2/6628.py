#include<bits/stdc++.h>
using namespace std;
string str,str2;
int main()
{
    int test,tc=1,i,j,n,cap,len,c;
    vector<int>vec;
    cin>>test;
    while(test--)
    {
        cin>>str;
        len=str.length();
        str2="";
        for(i=len-1; i>=0; i--)
        {
            if(str[i]!='+')
            {
                str2=str.substr(0,i+1);
                break;
            }
        }
        if(str2.length()==0)
        {
            cout<<"Case #"<<tc++<<": 0"<<endl;
            continue;
        }
        len=str2.length();
        c=0;
        for(i=0; i<len; i++)
        {
            if(str2[i]=='-')
            {
                while(str2[i]=='-' && i<len)
                    i++;
                c++;
                i--;
            }
            else if(str2[i]=='+')
            {
                while(str2[i]=='+' && i<len)
                    i++;
                c++;
                i--;
            }
        }
        cout<<"Case #"<<tc++<<": "<<c<<endl;
    }
    return 0;
}
