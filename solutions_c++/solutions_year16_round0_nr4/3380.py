#include<bits/stdc++.h>
using namespace std;
typedef long long int LL;
bool visited[1<<16];
vector<vector<int> >vec[17];
vector<int>prime;
LL poww(LL K,LL C)
{
	LL ans=1LL;
	while(C)
	{
		if(C&1)
		ans=ans*K;
		K*=K;
		C>>=1;
		
	}
	return ans;
}
int main()
{
	ifstream cin("Q4S.in");
	ofstream cout("Q4SA.txt");
	int i,j,t,ind=1,k;
	LL m,n,c,s,a,b,K,C,S;
	
	cin>>t;
	while(t--)
	{
		cin>>K>>C>>S;
		a=poww(K,C-1);
		cout<<"Case #"<<ind++<<": ";
		b=1LL;
		for(i=1;i<=K;i++)
		{
			cout<<b<<" ";
			b+=a;
		}
		cout<<endl;
	}
	
}
