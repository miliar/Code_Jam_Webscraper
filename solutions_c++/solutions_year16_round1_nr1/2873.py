
#include <bits/stdc++.h>
using namespace std;
#ifndef M
#define M 1000000007
#endif
typedef pair<int,int>pp;
typedef std::vector<pp> vpp;
typedef long long ll;
#ifndef pb
#define pb push_back 
#endif 
int min(int x,int y){return(x<y)?x:y;}
int max(int x,int y){return(x>y)?x:y;}
int main(int argc, char const *argv[])
{
	string s;
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		printf("Case #%d: ",i );
		cin>>s;
		int len=s.size();
		string k;
		k.push_back(s[0]);
		for(int i=1;i<len;i++)
		{
			if(s[i]>=k[0])
				k=s[i]+k;
			else
				k=k+s[i];
		}
		cout<<k<<'\n';
	}
	return 0;
}