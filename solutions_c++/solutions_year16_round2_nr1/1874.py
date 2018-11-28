#include <bits/stdc++.h>
using namespace std;
#define sd(x) scanf("%d",&x)
#define pd(x) printf("%d\n",x)
#define sl(x) scanf ("%lld",&x)
#define pl(x) printf("%lld\n",x);
#define fr(i,n) for(i=0;i<n;i++)
#define frn(i,n) for(i=0;i<=n;i++)
#define fro(i,m) for(i=1;i<m;i++)
#define frr(i,n) for(i=n-1;i>=0;i--)
#define mod 1000000007
#define ll long long 
#define pb push_back
#define vi vector<int>
#define vl vector<long long>

int main()
{
	int t;
	sd(t);
	int t1 = t;
	while(t--)
	{
		map<char,int> mp;
		mp.clear();
		int count[1002],i,cnt[1002];
		fr(i,29)
		{
			count[i] = 0;
			cnt[i] = 0;
		}
		string a;
		cin>>a;
		for(i=0;i<a.length();i++)
		{
			mp[a[i]]++;
		}
		cnt[8]+=mp['G'];
		mp['E']-=mp['G'];
		mp['I']-=mp['G'];
		mp['H']-=mp['G'];
		mp['T']-=mp['G'];
		cnt[0]+=mp['Z'];
		mp['E']-=mp['Z'];
		mp['R']-=mp['Z'];
		mp['O']-=mp['Z'];
		cnt[6]+=mp['X'];
		mp['I']-=mp['X'];
		mp['S']-=mp['X'];
		cnt[7]+=mp['S'];
		mp['E']-=mp['S'];
		mp['V']-=mp['S'];
		mp['E']-=mp['S'];
		mp['N']-=mp['S'];
		cnt[5]+=mp['V'];
		mp['F']-=mp['V'];
		mp['I']-=mp['V'];
		mp['E']-=mp['V'];
		cnt[4]+=mp['F'];
		mp['O']-=mp['F'];
		mp['U']-=mp['F'];
		mp['R']-=mp['F'];
		cnt[2]+=mp['W'];
		mp['O']-=mp['W'];
		mp['T']-=mp['W'];
		cnt[3]+=mp['T'];
		mp['H']-=mp['T'];
		mp['R']-=mp['T'];
		mp['E']-=mp['T'];
		mp['E']-=mp['T'];
		cnt[1]+=mp['O'];
		mp['N']-=mp['O'];
		mp['E']-=mp['O'];
		cnt[9]+=(mp['N'])/2;
		printf("Case #%d: ",t1-t);
		for(i=0;i<=9;i++)
		{
			for(int j=0;j<cnt[i];j++)
				printf("%d",i);
		}
		printf("\n");
	}
	return 0;
}