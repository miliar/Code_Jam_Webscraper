#include<bits/stdc++.h>
using namespace std;
int t,t0,i,cnt;
string str;
char c;
int main()
{
    freopen("file.out","w",stdout);
    cin>>t;
    t0=1;
    while(t--)
    {
        cin>>str;
        cnt=0;
        c=str[0];
        for(i=1;i<str.length();i++)
        {
            if(str[i]==c)
                continue;
            c=str[i];
            cnt++;
        }
        if(str[str.length()-1]=='-') cnt++;
        cout<<"Case #"<<t0++<<": "<<cnt<<endl;
    }
}