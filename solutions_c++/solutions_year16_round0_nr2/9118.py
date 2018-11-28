#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("output.txt", "w", stdout);
    long long int i,j,k,l,cnt,t,v=1;
    string s;
    char ch;
    cin>>t;
    while(t--)
    {
        cin>>s;
        l=s.length();cnt=0;
        while(s[l-1]=='+')l--;
        if(l==0){cout<<"Case #"<<v++<<": "<<cnt<<endl;}
        else
        {
            ch=s[0];
            cnt=1;
            for(i=1;i<l;i++)
            {
                if(ch!=s[i])
                {
                    ch=s[i];
                    cnt++;
                }
            }
            cout<<"Case #"<<v++<<": "<<cnt<<endl;        }

    }


    return 0;
}
