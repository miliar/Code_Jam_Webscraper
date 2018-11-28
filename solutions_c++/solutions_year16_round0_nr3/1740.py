#include <bits/stdc++.h>
using namespace std;
bool np[100000010];
vector<int> ps;
string binary(int v,int len)
{
	string s;
	while(len--)
	{
		s+=(v&1)?'1':'0';
		v>>=1;
	}
	reverse(s.begin(),s.end());
	return s;
}
int check(const string &v,int base)
{
	__int128 iv=0;
	for(int i=0;i<(int)v.size();i++)
	{
		iv=iv*(__int128)base+(__int128)(v[i]=='1');
		//cout<<(long long)(iv/(long long)(1e18));
		//cout<<(long long)(iv%(long long)(1e18))<<endl;
	}
	//cout<<v<<": ";
	//cout<<(long long)(iv/(long long)(1e18));
	//cout<<(long long)(iv%(long long)(1e18))<<endl;
	for(int i=0; i<(int)ps.size() && ((__int128)ps[i])*ps[i]<=iv; i++)
		if(iv%ps[i]==0)
			return ps[i];
	return -1;
}
bool proc(string v)
{
	vector<int> res;
	for(int i=2;i<=10;i++)
	{
		int tmp=check(v,i);
		if(tmp==-1) return false;
		res.push_back(tmp);
	}

	cout<<v;
	for(int i=0;i<(int)res.size();i++)
		cout<<' '<<res[i];
	cout<<'\n';
	return true;
}
int main()
{
	//ios::sync_with_stdio(0);
	//cin.tie(0);

	for(long long i=2;i<=100000000;i++)
		if(np[i]==0)
		{
			for(long long j=i*i;j<=100000000;j+=i)
				np[j]=1;
			ps.push_back(i);
		}

	int T,no=0;
	cin>>T;
	while(T--)
	{
		int n,j;
		cin>>n>>j;
		cout<<"Case #"<<++no<<":\n";
		for(int i=0;j>0;i++)
		{
			string s="1"+binary(i,n-2)+"1";
			if(proc(s)) j--;
		}
	}
}