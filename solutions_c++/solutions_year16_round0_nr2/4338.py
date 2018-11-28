#include<bits/stdc++.h>
using namespace std;
int solve(string s)
{
    int count=0,i,j;
    bool flag;
    while(true)
    {
        flag=true;
        for(i=0;i<s.length();i++)
        {
            if(s[i]=='-')
                flag=false;
        }
        if(flag)
            break;
        i=0;
        if(s[0]=='+')
        {
           while(s[i]!='-' and i<s.length())
           {
                s[i]='-'; 
                i++;
           }
              
        }
        else
        {
            while(s[i]!='+' and i<s.length())
            {
                 s[i]='+'; 
                 i++;
             }
        }
        count++;
    }
    return count;
}
int main()
{
    int t;
    cin>>t;
    string s;
    for(int i=1;i<=t;i++)
    {
       cin>>s;
       cout<<"Case #"<<i<<": ";
       cout<<solve(s)<<endl;
    }
    return 0;
}
