#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int j=1;
    while(t--)
    {
        string s;
        long long int c=0;
        cin>>s;long long int a=0;
        for(int i=0;i!=s.length();i++)
           {
               if(i==0&&s[i]=='-')
                c=1;
               if(i>0&&s[i]=='-'&&s[i-1]=='+')
                c+=2;
           }
            cout<<"Case #"<<j<<": "<<c<<"\n";j++;
    }
}
