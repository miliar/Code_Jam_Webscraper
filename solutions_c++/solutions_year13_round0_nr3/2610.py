#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <utility>
#include <cstring>
#include <string>
#include <cstdio>
#include <stdlib.h>
#include <cmath>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;

#define pb push_back
#define mp make_pair
#define S second
#define F first
#define INF 2000000000
#define MEMSET_INF 127

int pal(int n)
{
	char c[1000];
	int siz=sprintf(c,"%d",n);

	for (int i = 0; i < siz/2; ++i)
	{
		if(c[siz-1-i]!=c[i])
			return 0;
	}
	return 1;
}
int main(int argc, char const *argv[])
{
	int t;
	cin>>t;
	for (int i = 0; i < t; ++i)
	{
		int a,b;
		int total=0;
		cin>>a>>b;
		for (int j = a; j <=b; ++j)
		{
			if(sqrt((double)j)==floor(sqrt((double)j)))
				if(pal((int)sqrt((double)j))&&pal(j))
					total++;
		}
		printf("Case #%d: %d\n",i+1,total);
	}
	return 0;
}
