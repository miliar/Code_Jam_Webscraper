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
int a[1000001];
int main()
{
    freopen("B-large.in", "r",stdin);
    freopen("B-op-large.txt", "w" ,stdout);
    int t;
    Input(t);
    int z=t;
    while(t--)
    {
        int n;
        Input(n);
        //int a[n];
        int i;
        int maxi=0;
        for(i=0;i<n;i++)
        {
            Input(a[i]);
            if(a[i]>maxi)
                maxi=a[i];
        }
        int div,count=0,rem,ans=maxi;
        for(i=1;i<maxi;i++)
        {
            count=0;
            for(int j=0;j<n;j++)
            {
                if(a[j]>i)
                {
                    div=a[j]/i;
                    rem=a[j]%i;
                    if(rem!=0)
                        count+=div;
                    else
                        count+=div-1;
                }
            }
            ans=min(ans,i+count);

        }
       cout<<"Case #"<<z-t<<": "<<ans<<"\n";
    }
}
