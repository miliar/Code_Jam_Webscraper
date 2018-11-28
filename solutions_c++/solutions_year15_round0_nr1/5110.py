#include <iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;
#define lld long long int
char str[1005];
int main()
{
    lld i,j,n,u,in,t,l,s;
    freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
    cin>>t;
    for(l=1;l<=t;l++)
    {
        u=0;
        in=0;
        cin>>s>>str;
        for(i=0;i<=s;i++)
        {
            if(str[i]!='0')
            {
                if(u>=i)
                {
                    u+=(str[i]-'0');
                }
                else
                {
                    in+=(i-u);
                    u=i+(str[i]-'0');
                }
            }
        }
        cout<<"Case #"<<l<<": "<<in<<endl;
    }
	return 0;
}
