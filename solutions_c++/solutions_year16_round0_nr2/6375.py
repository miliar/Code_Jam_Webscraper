#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<string>
#include<set>

#define pis pair<int,string>
#define x first
#define y second
using namespace std;

bool pancake[101] ;
int solve(int n)
{
	int ans = 0;
	for(int i=0;i<n;i++)
	{
		if(pancake[i] == 0)
		{
			ans += 1;
			for(int j=i;j<n;j++)
			{
				pancake[j] ^= 1; 
			}
		}
	}
	return ans;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int tCase;
	string S;
	scanf("%d",&tCase);
	for(int i=1;i<=tCase;i++)
	{
		printf("Case #%d: ",i);
		cin >> S;
		reverse(S.begin() , S.end());
		for(int i=0;i<S.size();i++)
		{
			pancake[i] = (S[i] == '+'?1:0);
		}
		printf("%d\n",solve(S.size()));
	}
	return 0;
}