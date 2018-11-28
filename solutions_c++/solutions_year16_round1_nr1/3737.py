#include<bits/stdc++.h>
using namespace std;
string str,str1;
int main()
{
    int test,tc=1,i,x,y;
    cin>>test;
    while(test--)
    {
        cin>>str;
        str1=str.substr(0,1);
        for(i=1; i<str.length(); i++)
        {
            x=int(str[i]);
            y=int(str1[0]);
            if(x>=y)
                str1=str.substr(i,1)+str1;
            else
                str1+=str.substr(i,1);
        }
        cout<<"Case #"<<tc++<<": "<<str1<<endl;
    }
    return 0;
}
