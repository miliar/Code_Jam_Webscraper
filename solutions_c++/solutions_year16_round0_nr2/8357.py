#include<iostream>
#include<string>
using namespace std;
int main()
{
    ios::sync_with_stdio(false);
    int t,i,c,j;
    string str;
    cin>>t;
    for(j=1;j<=t;j++)
    {
        cin>>str;
        str+='+';
        c=0;
        for(i=0;i<str.length()-1;i++)
            if((str[i]=='+'  &&  str[i+1]=='-') || (str[i]=='-' && str[i+1]=='+'))
                c++;
        cout<<"Case #"<<j<<": "<<c<<"\n";
    }
    return 0;
}
