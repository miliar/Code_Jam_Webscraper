#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <bitset>
#include <sstream>
#include <string>

#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>

#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

#define FILL(arr,n) memset(arr,n,sizeof(arr))
#define FORUP(i,m,n) for(int i=(m); i<(n); i++)
#define FORDOWN(i,m,n) for(int i=(m)-1; i>=(n); i--)

#define PB push_back
#define MP make_pair
#define F first
#define S second

#define INF 2000000000
#define EPS 1e-11
#define PI acos(-1.0)
#define MAX_N 1000005
using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<pii> vii;

int N;
bool isConsonant(char a)
{
	if (a == 'a' || a == 'i' || a == 'u' || a == 'e' || a == 'o')return false;
	return true;
}

bool maxConsonant(string kata)
{
	int maxConsonant = 0;
	int consonantNow = 0;
	bool nowConsonant = false;
	if(isConsonant(kata[0]))
	{
		nowConsonant = true;
		maxConsonant = consonantNow = 1;
	}
	for(int i = 1;i < kata.length();i++)
	{
		if(isConsonant(kata[i]))
		{
			nowConsonant = true;
			consonantNow++;
			maxConsonant = max(maxConsonant,consonantNow);
		}
		else if(nowConsonant)
		{
			nowConsonant = false;
			consonantNow = 0;
		}
		if(maxConsonant >= N)
		{
			return true;
		}
	}
	if(maxConsonant >= N)return true;
	return false;
}

int
main()
{
	int T;
	string kata;
	scanf("%d", &T);
	for(int tc = 1;tc <= T;tc++)
	{
		cin >> kata >> N;
		int nvalue = 0;
		for(int i = 0;i < kata.length();i++)
		{
			string nows = "";
			nows += kata[i];
			bool isOke = false;
			if(maxConsonant(nows))
			{
				isOke = true;
				nvalue++;
			}
			for(int j = i+1;j < kata.length();j++)
			{
				nows += kata[j];
				if(isOke)nvalue++;
				else if(maxConsonant(nows))
				{
					isOke = true;
					nvalue++;
				}
			}
		}
		printf("Case #%d: %d\n",tc,nvalue);
	}
return 0;
}