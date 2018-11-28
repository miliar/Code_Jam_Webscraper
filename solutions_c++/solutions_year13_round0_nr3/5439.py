#include<iostream>	
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<string>
#include<algorithm>
#include<functional>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<cassert>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned int UINT;
int gcd(int a,int b) { while (b > 0) { a = a % b; a ^= b; b ^= a; a ^= b;} return a; }
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define MOD 1000000007

bool ispalin(int x)
{
	//given a integer return true if it is a palindrome
	int i=x;
	int y=0;
	while(i>0)
	{
		y=y*10+(i%10);
		i=i/10;
	}
	return (x==y);
}
int main()
{
	//fair and square - must be a palindrome and must be the square of a palindrome.
	
	//generate all
	vi v;
	for(int i=1;i<=31;i++)
	{
		if(ispalin(i))
		{
			if(ispalin(i*i))
			{
				v.push_back(i*i);
			}
		}
	}
	
/*	for(int i=0;i<v.size();i++)
		cout<<v[i]<<" ";
	cout<<endl;
*/
	int tc;
	scanf("%d",&tc);
	int p=0;
	while(tc--)
	{
		p++;
		int a,b;
		int ans=0;
		printf("Case #%d: ",p);
		scanf("%d%d",&a,&b);
		for(int i=0;i<v.size();i++)
		{
			if(v[i]>=a && v[i]<=b)
				ans++;
		}
		cout<<ans<<endl;
	}	
	return 0;
}
		
