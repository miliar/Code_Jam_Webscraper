//property of varun hasija
#include<bits/stdc++.h>
using namespace std;
#define ll long long
inline void input(ll &N)
{
	ll ch;
	N=0;

	while((ch<'0' || ch>'9') && ch!='-' && ch!=EOF)
		ch=getchar();

	do
		N=(N<<3)+(N<<1)+(ch-'0');
	while((ch=getchar())>='0' && ch<='9');

	return;
}
inline void Input(int &N)
{
	int ch;
	N=0;

	while((ch<'0' || ch>'9') && ch!='-' && ch!=EOF)
		ch=getchar();

	do
		N=(N<<3)+(N<<1)+(ch-'0');
	while((ch=getchar())>='0' && ch<='9');

	return;
}
int main()
{
    freopen("A-large.in", "r",stdin);
    freopen("A-op-large.txt", "w" ,stdout);
    int t;
    Input(t);
    int z=t;
    while(t--)
    {
        int n;
        Input(n);
        string s;
        cin>>s;
        int count=s[0]-'0';
        int ans=0,i;
        for(i=1;i<=n;i++)
        {
            if(s[i]-'0'!=0 and count<i)
            {
                ans+=(i-count);
                count+=+(i-count);
                count+=s[i]-'0';
            }
           else if(s[i]-'0'!=0)
           {
               count+=s[i]-'0';
           }
        }
        cout<<"Case #"<<z-t<<": "<<ans<<"\n";
    }
}
