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
 	
 	bool pc(int n)
 	{
 		stringstream ss;
 		ss<<n;
 		string a;
 		a=ss.str();
 		int k=a.size();
 		for (int i = 0; i < k; i += 1)
 		{
 			if(a[i] != a[k-i-1]) return false;
 		}
 		return true;
 	}
 	
    int main()
    {
    	 int n;
    	 cin>>n;
    	 for (int z = 1; z <= n; z += 1)
    	 {
    	 	int l,u;
    	 	cin>>l>>u;
    	 	int count=0;
    	 	for (int i = l; i <= u; i += 1)
    	 	{
    	 		double sq=sqrt(i);
    	 		if(pc(i) && (floor(sq)==ceil(sq)) && pc(floor(sq))) count++;
    	 	}
    	 	cout<<"Case #"<<z<<": "<<count<<endl;
    	 }
       return 0;
    }
