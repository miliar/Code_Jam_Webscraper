#include<iostream>
#include<map>
#include<string>
#include<sstream>
using namespace std;
int num=1;

void Gao()
{
	int ans=0LL,already=0;
	long long n=0LL,base=0LL;
	printf("Case #%d: ",num++);
	
	cin>>n;
	base=n;
	if (n==0)
	{
		cout<<"INSOMNIA"<<endl;
		return ;
	}
	map<char ,int> mp;
	string st="";
	stringstream ss;
	while (true)
	{
		ss.clear();
		ss<<n;
		ss>>st;
		for (int i=0;i<st.length();i++)
		{
			if (mp.find(st[i])==mp.end())
			{
				mp[st[i]]=12450;
				already++;
			}
		}
		if (already==10)
		{
			cout<<st<<endl;
			return;
		}
		n=n+base;
	}	
}
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;
	cin>>T;
	while (T--)
		Gao();
	return 0;
} 
