#include <iostream>
#include <cstring>
#include <string>
using namespace std;
int test = 1;
int alpha[33];
void solve()
{
	double res;
	int k,l,s;
	cin >> k >> l >> s;
	bool bb = true;
	string s1,s2;
	cin >> s1;
	cin >> s2;
	for( int i = 0 ; i < k ; i++ )
	{
		alpha[s1[i]-'A']++;
	}
	res = 1;
	for( int i = 0 ; i < l ; i++ )
	{
		if(alpha[s2[i]-'A'] == 0 ) bb = false;
		res *= ((double)alpha[s2[i]-'A']/(double)k);
	}
	double maxi,expect;
	expect = (s-l+1)*res;

	int matched = 0;
	string temp1,temp2;
	double res_temp=1;
	for( int i = 1 ; i < l ; i++ )
	{
		temp1 = s2.substr(0,i);
		temp2 = s2.substr(l-i);
		if(temp1.compare(temp2)==0)
		{
			matched = i;
			res_temp=1;
		}
	}
	
	int cnt=1;
	int ss = s-l;
	while(ss-(l-matched)>=0)
	{
		ss -= (l-matched);
		cnt++;
	}
	maxi = cnt;
	if(!bb) res = 0;
	else res = maxi-expect;
	printf("Case #%d: %lf\n",test++,res);
	return;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t;
	cin >> t;
	while(t--)
	{
		memset(alpha,0,sizeof(alpha));
		solve();
	}
	return 0;
}