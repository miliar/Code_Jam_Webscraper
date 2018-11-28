#include<iostream>
#include<string>
using namespace std;

int main()
{
    int t,s,i,t2;
    string s1,s2;
    cin>>t;
    t2=t;
    while(t--)
    {
        cin>>s1;
        s=s1.length();
        s2=s1[0];
        for(i=1;i<s;i++)
        {
            if(s2[0]<=s1[i])
            s2=s1[i]+s2;
            else
            s2=s2+s1[i];
        }
        cout<<"Case #"<<t2-t<<": "<<s2<<endl;
    }
    return 0;
}
