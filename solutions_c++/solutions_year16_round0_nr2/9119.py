#include <iostream>
#include <string>
#include <string.h>

using namespace std;

#define lli long long int
int main() {
    lli test;
    cin>>test;
    lli k;
    for(k=1;k<=test;k++)
    {
        cout<<"Case #"<<k<<": ";
        string s;
        char cpy[102];
        cin>>s;
        // cout<<s[0]<<endl;
        cpy[0]=s[0];
        // cout<<"hello";
        // cout<<"i am here"<<cpy<<" lskjd"<<endl;
        // cout<<cpy<<endl;
        lli i,j=1;
        for(i=1;i<s.length();i++)
        {
            // cout<<"i="<<i<<"  ";
            if(s[i]!=s[i-1])
            {
                // cout<<"i="<<i<<" "<<"j="<<j<<endl;
                cpy[j]=s[i];
                // cout<<cpy[j]<<endl;
                j++;
            }
        }
        cpy[j]='\0';
        // cout<<cpy<<endl;
        lli ans=0;
        for(i=0;i<strlen(cpy);i++)
        {
            if(i==0 && cpy[i]=='-')
            {
                ans+=1;
            }
            else
            {
                if(cpy[i]=='-')
                {
                    ans+=2;
                }
            }
        }
        cout<<ans<<endl;
    }
	return 0;
}
