#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define mp make_pair
#define pi pair<ll,ll>
#define MOD 1000000007
bool b[2010];
char c[2010];
ll cnt[26];
ll ans[10];
int main()
{
	ll t,n;
	cin>>t;
	string s;
	ll z=1;
	while(t--)
	{
		cin>>c;
		n=strlen(c);
		for(int i=0;i<26;i++)
		{
			cnt[i]=0;
		}
		//memset(b,0,sizeof(b));
		for(int i=0;i<n;i++)
		{
			cnt[c[i]-'A']++;
		}
		//cout<<cnt[19]<<endl;
		ans[2]=cnt[22];
		cnt[22]=0;
		cnt[19]-=ans[2];
		cnt[14]-=ans[2];
		ans[6]=cnt[23];
		cnt[23]-=ans[6];
		cnt[18]-=ans[6];
		cnt[8]-=ans[6];
		ans[8]=cnt[6];
		cnt[6]=0;
		cnt[4]-=ans[8];
		cnt[8]-=ans[8];
		cnt[7]-=ans[8];
		cnt[19]-=ans[8];
		//cout<<cnt[19]<<endl;
		ans[3]=cnt[19];
		cnt[19]=0;
		cnt[7]-=ans[3];
		cnt[17]-=ans[3];
		cnt[4]-=2*ans[3];
		ans[0]=cnt[25];
		cnt[25]=0;
		cnt[4]-=ans[0];
		cnt[17]-=ans[0];
		cnt[14]-=ans[0];
		ans[4]=cnt[20];
		cnt[20]=0;
		cnt[5]-=ans[4];
		cnt[14]-=ans[4];
		cnt[17]-=ans[4];
		ans[7]=cnt[18];
		cnt[18]=0;
		cnt[21]-=ans[7];
		ans[5]=cnt[21];
		cnt[8]-=ans[5];
		ans[1]=cnt[14];
		ans[9]=cnt[8];
		cout<<"Case #"<<z<<": ";
		for(int i=0;i<10;i++)
		{
			for(int j=0;j<ans[i];j++)
			{
				cout<<i;
			}
		}
		cout<<endl;
		z++;
	}
	return 0;
}