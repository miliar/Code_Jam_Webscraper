#include<iostream>
#include<string>

using namespace std;

int main()
{
    int t,i,j,cnt;
    string s;

    cin>>t;

    for(i=1;i<=t;i++)
    {
        cin>>s;
        cout<<"Case #"<<i<<": ";

        if(s.at(0)=='-')
            cnt=1;
        else
            cnt=0;
        for(j=1;j<s.length();j++)
        {
            if(s.at(j)=='-' && s.at(j-1)!='-')
                cnt+=2;
        }
        cout<<cnt<<endl;
    }
}
