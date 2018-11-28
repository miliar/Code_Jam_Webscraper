#include<bits/stdc++.h>
using namespace std;
int main ()
{

    int t;
    cin>>t;
    int n = t;
    while(t--)
    {
        int shy;
        cin>>shy;
        char s[shy+1];
        cin>>s[0];
        int person= s[0]- '0';
        int frds =0;
        for(int i=1;i<=shy;i++)
        {
            cin>>s[i];
            if(person>=i&& s[i] - '0'!=0)
            {
                person+=(s[i] - '0');
              // cout<<i<<" "<<person<<endl;
            }
            else if(person<i&&s[i]-'0'!=0)
            {
                frds+=i-person;
                person = person+frds + (s[i] - '0');
             //  cout<<i<<" "<<person<<endl;
            }
        }
        cout<<"Case "<<"#"<<n-t<<": "<<frds<<endl;

    }
    return 0;

}
