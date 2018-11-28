#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<algorithm>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<cstring>
#include<map>
#include<iterator>
#define input freopen("input.txt", "r", stdin)
#define output freopen("output.txt", "w", stdout)
#define pb push_back
#define REP(i,n) for(int i = 0, _n = (n); i < _n; i++)
#define REPD(i,n) for(int i = (n) - 1; i >= 0; i--)
#define FOR(i,a,b) for(int i = (a), _b = (b); i <= _b; i++)
using namespace std;

const int inf = 0x7FFFFFFF;
const double eps = 1e-9L;
const double pi = acos(-1.0);
typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<string> vs;
typedef pair<string,int> psi;
typedef pair<int,int> pii;
typedef map<string,int> msi;
typedef map<int,int> mii;
typedef long long ll;
typedef long double ld;

using namespace std;
 	
 	
    int main()
    {
    	int t;
    	cin>>t;
    	for (int z = 1; z <= t; z += 1)
    	{
    		int n,m;
    		cin>>n>>m;
    		int maxr[105]={-inf},maxc[105]={-inf},inp[105][105];
    		for (int i = 0; i < n; i += 1)
    		{
    			for (int j = 0; j < m; j += 1)
    			{
    				cin>>inp[i][j];
    				maxr[i] = max(maxr[i],inp[i][j]);
    				maxc[j] = max(maxc[j],inp[i][j]);
    			}
    		}
    		
    		bool check=true;
    		for (int i = 0; i < n; i += 1)
    		{
    			for (int j = 0; j < m; j += 1)
    			{
    				if(maxr[i]>inp[i][j] && maxc[j]>inp[i][j]) check=false;
    			}
    		}
    		
    		cout<<"Case #"<<z;
    		if(check) cout<<": YES\n";
    		else cout<<": NO\n";
    		
    	}
       return 0;
    }
