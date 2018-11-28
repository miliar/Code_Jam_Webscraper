#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <set>
#include <vector>
#include <queue>
#include <map>
using namespace std;

#define forn(i, n) for(int i = 0; i < ((int) n); i++)
#define EPS 0.0000000000000001

map<string, int> nums;
int cn;
int wordmaps[2560];
string line[2560];

void procesar(string s, int i)
{
	s+=" ";
	int ss=s.size(), it=0;
	string start;
	while(it<ss)
	{
		if(s[it]==' ')
		{
			if(!nums.count(start))
			{
				nums[start] = cn;
				cn++;
			}
			wordmaps[nums[start]]|=(1<<i);
			
			start="";
		}
		else
		{
			start+=s[it];
		}
		it++;
	}
}

int main()
{	
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int T;
	cin >> T;
	
	forn(tc, T)
	{
		int N;
		cin >> N;
		
		string basura;
		getline(cin, basura);
		
		forn(i, 2560) wordmaps[i]=0;
		nums.clear();
		cn=0;
		
		forn(i, N) getline(cin, line[i]);
		
		forn(i, N) procesar(line[i], i);
		int ans = cn;
		
		for(int i=1; i<(1<<N); i+=4)
		{
			int di=(1<<N)-i-1, cur=0;
			forn(j, cn)
			{
				if((wordmaps[j]&i) && (wordmaps[j]&di)) cur++;
			}
			ans=min(ans, cur);
		}
		
		cout << "Case #" << tc+1 << ": ";
		cout << ans << endl;
	}
	
}
