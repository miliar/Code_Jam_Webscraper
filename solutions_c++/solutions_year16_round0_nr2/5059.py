#include<iostream>
#include<string>
#include<cstdio>

using namespace std;

int cs=1;

int main()
{
    FILE *in=freopen("bl.in","r",stdin);
    FILE *out =freopen("Blarge.txt","w",stdout);

    int t,i;
    long long int ans;
    string s;

    cin>>t;

    while(t--)
    {
        cin>>s;

        if(s[0]!='-')
            ans=0;
        else
            ans=1;

        for(i=1;i<s.length();i++)
        {
            if(s[i]!='+' && s[i-1]!='-')
                ans+=2;
        }
        cout<<"Case #"<<cs<<": "<<ans<<endl;
         cs++;
    }

   fclose(in);
   fclose(out);

   return 0;
}
