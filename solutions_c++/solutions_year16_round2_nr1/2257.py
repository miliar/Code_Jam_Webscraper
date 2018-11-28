#include <cstdio>
#include <iostream>
#include <queue>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <set>
#include <stack>
#include <cctype>
#include <fstream>
#include <sstream>
#include <bitset>
#include <utility>
#include <map>
#include <list>

using namespace std;

#define loop(x,y,z) for(int x=y;x<=z;x++)
#define pi acos(-1.0)
#define sz(a) (int)(a).size()
#define NMAX 2147483647
#define LMAX 9223372036854775807LL
#define pb push_back
#define mp make_pair
#define ll long long
#define pf printf
#define mem(x,y) memset(x,y,sizeof(x))
#define rep(x,y) for(int x=1;x<=y;x++)
#define pii pair<int,int>
#define gi(k) scanf("%d",&k)
#define PI acos(-1.0)
#define eps 1e-8
#define fi first
#define sc second
#define inf 1e13
#define endl "\n"
#define FO(i,n) for(int i = 0; i < n; i++)

const int INF = (int) 1e9;
const long long INF64 = (long long) 1e18;

#pragma comment (linker,"/STACK:16777216")
#pragma warning(disable:4786)

int Set(int N , int pos){return N = N | (1 << pos); }
int Reset(int N , int pos){return N = N & ~(1 << pos); }
bool check(int N, int pos){return (bool) (N & (1<<pos)); }

const int mx=1<<29;
int ans,sum,t,n,k,m;
string s;
int flag[55],ct[55];
std::vector<int> v[55];

int dx[] = {0,1,-1,0,0};
int dy[] = {0,0,0,1,-1};

int main()
{
    //ios::sync_with_stdio(false);cin.tie(0);
    freopen("00_input.txt", "r", stdin);freopen("00_output.txt", "w", stdout);
	
    cin >> t;

    rep(ii,t)
    {
    	FO(i,26) { v[i].clear(); }

    	cin >> s;

    	mem(ct,0); mem(flag,0);

    	FO(i,s.size())
    	{
    		v[s[i]-'A'].pb(i);
    	}

    	FO(i,s.size())
    	{
    		if(s[i] == 'Z')
    		{
    			s[i] = '#';

    			s[ v[4][flag[4]] ] = '#'; flag[4]++;
    			s[ v['R'-'A'][flag['R'-'A']] ] = '#';flag['R'-'A']++;
    			s[ v['O'-'A'][flag['O'-'A']] ] = '#';flag['O'-'A']++;

    			ct[0]++;
    		}

    		else if(s[i] == 'W')
    		{
    			s[i] = '#';

    			s[ v['T'-'A'][flag['T'-'A']] ] = '#';flag['T'-'A']++;
    			s[ v['O'-'A'][flag['O'-'A']] ] = '#';flag['O'-'A']++;

    			ct[2]++;
    		}

    		else if(s[i] == 'U')
    		{
    			s[i] = '#';

    			s[ v['F'-'A'][flag['F'-'A']] ] = '#';flag['F'-'A']++;
    			s[ v['O'-'A'][flag['O'-'A']] ] = '#';flag['O'-'A']++;
    			s[ v['R'-'A'][flag['R'-'A']] ] = '#';flag['R'-'A']++;

    			ct[4]++;
    		}

    		else if(s[i] == 'X')
    		{
    			s[i] = '#';

    			s[ v['S'-'A'][flag['S'-'A']] ] = '#';flag['S'-'A']++;
    			s[ v['I'-'A'][flag['I'-'A']] ] = '#';flag['I'-'A']++;

    			ct[6]++;
    		}

    		else if(s[i] == 'G')
    		{
    			s[i] = '#';

    			s[ v['E'-'A'][flag['E'-'A']] ] = '#';flag['E'-'A']++;
    			s[ v['I'-'A'][flag['I'-'A']] ] = '#';flag['I'-'A']++;
    			s[ v['H'-'A'][flag['H'-'A']] ] = '#';flag['H'-'A']++;
    			s[ v['T'-'A'][flag['T'-'A']] ] = '#';flag['T'-'A']++;

    			ct[8]++;
    		}
    	}



    	FO(i,s.size())
    	{
    		if(s[i] == 'O')
    		{
    			s[i] = '#';
    		
    			s[ v['N'-'A'][flag['N'-'A']] ] = '#';flag['N'-'A']++;
    			s[ v['E'-'A'][flag['E'-'A']] ] = '#';flag['E'-'A']++;

    			ct[1]++;
    		}

    		else if(s[i] == 'R')
    		{
    			s[i] = '#';

    			s[ v['T'-'A'][flag['T'-'A']] ] = '#';flag['T'-'A']++;
    			s[ v['H'-'A'][flag['H'-'A']] ] = '#';flag['H'-'A']++;
    			s[ v['E'-'A'][flag['E'-'A']] ] = '#';flag['E'-'A']++;
    			s[ v['E'-'A'][flag['E'-'A']] ] = '#';flag['E'-'A']++;

    			ct[3]++;
    		}

    		else if (s[i] == 'F')
    		{
    			s[i] = '#';

    			s[ v['I'-'A'][flag['I'-'A']] ] = '#'; flag['I'-'A']++;
    			s[ v['V'-'A'][flag['V'-'A']] ] = '#'; flag['V'-'A']++;
    			s[ v['E'-'A'][flag['E'-'A']] ] = '#'; flag['E'-'A']++;

    			ct[5]++;
    		}

    		else if (s[i] == 'S')
    		{
    			s[i] = '#';

    			s[ v['E'-'A'][flag['E'-'A']] ] = '#'; flag['E'-'A']++;
    			s[ v['V'-'A'][flag['V'-'A']] ] = '#'; flag['V'-'A']++;
    			s[ v['E'-'A'][flag['E'-'A']] ] = '#'; flag['E'-'A']++;
    			s[ v['N'-'A'][flag['N'-'A']] ] = '#'; flag['N'-'A']++;
    			
    			ct[7]++;
    		}
    	}

    	FO(i,s.size())
    	{
    		if (s[i] == 'I')
    		{
    			ct[9]++;
    		}
    	}

    	pf("Case #%d: ",ii);

    	FO(i,10)
    	{
    		while(ct[i]){pf("%d",i); ct[i]--; }
    	}

    	pf("\n");
    }


    return 0;
}
