									/*	In the name of God	*/
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
#include <sstream>
#include <bitset>
#include <map>
#include <set>
#include <queue>
#include <stack>

#define rep(i,n) for((i)=0;(i)<(n);(i)++)
typedef long long ll;

using namespace std;

int n;
char s[201][201];
vector<char> a[201];
vector<int> b[201];
int main(){
	int tc,i,j,k,x,sum,r;
	bool f;
	freopen("A-small-attempt0 (1).in","r",stdin);
	freopen("output.txt","w",stdout);
	
	scanf("%d",&tc);
	for (int tci = 1; tci <= tc; tci++)
	{
		//TODO get input & stuff
		scanf("%d",&n);
		for (int i = 0; i < n; i++)
		{
			scanf("%s",s[i]);
			a[i].clear();
			b[i].clear();
		}
		f=0;
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; s[i][j]; j++)
			{
				x=j;
				while(s[i][j]==s[i][j+1])
					j++;
				a[i].push_back(s[i][x]);
				b[i].push_back(j-x+1);
			}
			if (a[i].size()!=a[0].size())
				f=1;
			for (int j = 0; j < a[i].size() && j<a[0].size(); j++)
				if (a[i][j]!=a[0][j])
					f=1;
		}
		r=0;
		if (!f)
			for (int j = 0; j < b[0].size(); j++)
			{
				sum=0;
				for (int i = 0; i < n; i++)
				{
					sum+=b[i][j];
				}
				x=(int)(sum/(double)n+.5);
				for (int i = 0; i < n; i++)
				{
					r+=abs(b[i][j]-x);
				}
			}

		printf("Case #%d: ",tci);
		//TO output results
		if (f)
			printf("Fegla Won");
		else
			printf("%d",r);
		printf("\n");
	}
	
	return 0;
}