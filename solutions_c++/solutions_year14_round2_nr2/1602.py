#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <climits>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>

#define pb push_back
#define ll long long
#define mp make_pair
#define f first
#define s second
#define all(x) x.begin(),x.end()
#define rall(x) x.rbegin(),x.rend()
#define pi acos(-1.0)
#define EPS 1e-9

using namespace std;

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int a,b,k,t,cs=0;cin>>t;
	while(t--){
		int ans=0;
		cin>>a>>b>>k;
		for(int i=0;i<a;i++){
			for(int j=0;j<b;j++){
				ans+=((i&j)<k && (i&j)>=0);
			}
		}
		cout<<"Case #"<<++cs<<": "<<ans<<"\n";
	}
	return 0;
}
