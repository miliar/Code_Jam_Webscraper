#include<bits/stdc++.h>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    int te;
    cin>>te;
    for(int t=1;t<=te;t++)
    {
        string s;
        cin>>s;
        int resp=0;
        int pos=0;
        if(s[0]=='-') resp++;
        while(pos<s.length() and s[pos]=='-')
        {
            pos++;
        }
        for(int i=pos;i<s.length();i++)
        {
            if(s[i]=='-')
            {
                resp+=2;
                while(i<s.length() and s[i]=='-')
                {
                    i++;
                }
            }
        }
        cout<<"Case #"<<t<<": "<<resp<<endl;
    }
    return 0;
}
