#include<iostream>
#include<string>
using namespace std;

main()
{
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        string s,t="";
        cin>>s;
        t=s[0];
        for(int j=1;j<s.length();j++)
        {
            if(t[0]<=s[j]) t = s[j]+t;
            else t=t+s[j];
        }
        cout<<"Case #"<<i<<": "<<t<<endl;
    }
    return 0;
}
