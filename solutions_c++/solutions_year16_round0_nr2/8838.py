#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long int t,a,len;
    string s;
    cin>>t;
    for(int g=0;g<t;g++)
    {   a=0;
        cin>>s;
        len=s.length();
        for(int i=0;i<(len-1);i++)
        {
            if(s[i]!=s[i+1])
                a++;
        }
        a=a+1;
        if(s[len-1]=='+')
            a=a-1;
        cout<<"Case #"<<g+1<<": "<<a<<endl;
    }
    return 0;
}