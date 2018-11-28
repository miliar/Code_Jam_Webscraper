#include <bits/stdc++.h>

#define pb push_back
#define pob pop_back
#define mp make_pair
#define ll long long
#define rep(i,x,y) for(i = x;i < y;i++)
#define repback(i,x,y) for (i = x - 1;i >= y;i--)
#define mod 1000000007

using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	int t,k=1;cin>>t;
	while(t--)
	{
		int x,i,temp,sum=0;cin>>x;
		string s;cin>>s;
		temp=(int)(s[0]-'0');
		rep(i,1,x+2)
		{
			if(temp<i)
			{
				temp++;
				sum++;
			}
			temp+=(int)(s[i]-'0');
		}
		cout<<"Case #"<<k++<<": "<<sum<<'\n';
	}
	return 0;
}