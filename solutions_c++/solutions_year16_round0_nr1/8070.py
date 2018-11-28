#include<bits/stdc++.h>
using namespace std;
#define F first
#define S second
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<pair<int,int> > vii;
set<int> s;
void parse(int x)
{
	while(x>0)
	{
		int l=x%10;
		s.insert(l);
		x/=10;
	}
	return;
}
int main()
{
	#ifndef ONLINE_JUDGE
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	#endif
	int n,t,k=1;
	scanf("%d",&t);
	while(t--)
	{
	s.clear();
	scanf("%d",&n);
	if(n==0)
	printf("Case #%d: INSOMNIA\n",k++);
	else
	{
	int cnt=1,N;
	while(true)
	{
		N=n*cnt;
		parse(N);
		if(s.size()==10)
		break;
		cnt++;
	}
	printf("Case #%d: %d\n",k++,N);
	}
	}
	return 0;
}
