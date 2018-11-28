#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include<iomanip>
using namespace std;

typedef long long ll;
typedef vector <int> vi;
typedef pair< int ,int > pii;
#define pb push_back
#define sz size()
#define ln length()
#define fore(i,a,b) for(int i=a;i<b;i++)
#define fores(i,a,b) for(int i=a;i<=b;i++)
#define ford(i,a,b) for(int i=a;i>=b;i--)
#define all(a) a.begin(),a.end()
#define mp make_pair
#define ff first
#define ss second
#define sc(a) scanf("%d",&a)
#define md 1000000007

int main() {
	freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	fore(z,0,t)
	{
		printf("Case #%d: ",z+1);
		string s;
		cin>>s;
		int k;
		cin>>k;
		int n = s.ln;
		int ans = 0;
		fore(i,0,n-k+1)
		{
		    if(s[i] == '-') {
                fore(j,i,i+k)
                {
                    if(s[j] == '-')
                        s[j] = '+';
                    else
                        s[j] = '-';
                }
                ans++;
		    }
		}
		bool found = false;
		fore(i,0,n)
		{
		    if(s[i] == '-') {
                found = true;
		    }
		}
		if(found) {
            cout << "IMPOSSIBLE" <<endl;
		}
		else {
            cout << ans << endl;
		}
	}
	return 0;
}
