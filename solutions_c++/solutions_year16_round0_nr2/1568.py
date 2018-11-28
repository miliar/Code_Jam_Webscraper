#include <iostream>
#include <vector>
#define MAXN 100000
#define INF 1000000000
using namespace std;

long long minflip(string s, int sz)
{
	int r = sz-1;
	while(r>=0 && s[r] == '+')
		r--;
	if(r<0)
		return 0;
	int l = r-1;
	while(l>=0 && s[l] == '-')
		l--;
	if(l<0)
		return 1;
	return minflip(s,l) + 2;
}


int main()
{
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		string s;
		cin>>s;
		long long ans = minflip(s, s.size());
		cout<<"Case #"<<t<<": "<<ans<<"\n";
	}
}
