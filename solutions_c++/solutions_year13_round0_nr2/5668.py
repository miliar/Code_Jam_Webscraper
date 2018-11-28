#include <algorithm> 
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctype.h>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector> 
using namespace std;

typedef long long             ll;
typedef vector<int>           vi;
typedef pair<int, int>        ii;
typedef vector<ii>            vii;
typedef map<int, int>         mii;
typedef set<int>              si;
typedef map<string, int>      msi;
typedef vector<bool>          vb;
typedef long double           ld;

#define rep(i, a, b)    for (int i = int(a); i <= int(b); i++)
#define repd(i, a, b)   for (int i = int(a); i >= int(b); i--)
//#define TR(c, it)       for (typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define pb              push_back
#define mp              make_pair
#define SIZE(c)         (int((c).size()))
#define LET(x, a)       __typeof(a) x = (a)
#define FOR(x, a, b)    for(LET(x,a); x!=(b); x++)
#define TR(cnt, it)     FOR(it, (cnt).begin(), (cnt).end())
 
#define vsort(v)        sort(v.begin(), v.end())
#define REDIRECT_INPUT  freopen("input.txt", "r", stdin)
#define REDIRECT_OUTPUT freopen("output.txt","w", stdout);
#define INF 2147483647  // 2^31-1

int arr[20][20];
int main()
{
	REDIRECT_INPUT;
	REDIRECT_OUTPUT;
	int T,M,N;
	int case1 = 1;
	cin>>T;
	while(T--)
	{
		bool flag1,flag2;
		flag1=flag2=false;
		cin>>M>>N;
		rep(i,0,M-1)
		rep(j,0,N-1)
		cin>>arr[i][j];
		bool invalid = false;
		rep(i,0,M-1)
		{
			if(invalid)
			break;
		rep(j,0,N-1)
		{
			flag1=flag2=false;
			if(arr[i][j]==1)
			{
				rep(k,0,M-1)
				if(arr[k][j]!=1)
				{
				    flag1 = true; 
					break;
				}
				
				rep(k,0,N-1)
				if(arr[i][k]!=1)
				{
					flag2 = true;
					break;
				}
				if(flag1 && flag2){
				printf("Case #%d: NO\n",case1);	invalid=true; break;}		
			}
		}
	}
			if(!invalid)
				printf("Case #%d: YES\n",case1);	
            case1++;
           }
	   } 				
