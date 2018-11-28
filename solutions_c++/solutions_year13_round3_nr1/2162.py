#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define bublic public
#define clr(x) memset((x), 0, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define sz size()
#define For(i, st, en) for(int i=(st); i<=(int)(en); i++)
#define Ford(i, st, en) for(int i=(st); i>=(int)(en); i--)
#define forn(i, n) for(int i=0; i<(int)(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)
#define fori(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); it++)


int qq;
int n;
int a[10240];
int b[10240];
int ans=0;
int cons=0,maxcons=0;
std::string s;

void main()
{
	freopen("a-small-attempt2.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	cin>>qq;
	
	forn(ii, qq)
	{
		printf("Case #%d: ", ii+1);
		cin>>s;
		cin>>n;
		int ans = 0;
		int temp=s.size();
		for(int i=0;i<s.size();i++){
			for(int j=0;j<=i;j++){
				maxcons=0;
				cons=0;
				for(int k=j;k<=i;k++){
					if(s[k]!='a'&&s[k]!='e'&&s[k]!='i'&&s[k]!='o'&&s[k]!='u'){
						cons++;
						if(maxcons<cons)maxcons=cons;
					}
					else {
						
						cons=0;
					}
				}
				
				if (maxcons>=n)ans++;
			}
		}

		printf("%d\n", ans);
	}



}
