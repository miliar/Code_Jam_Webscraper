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
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	int t,cs=0;cin>>t;
	while(t--){
		int n;cin>>n;vector<double> a(n),b(n),x,y;
		for(int i=0;i<n;i++)cin>>a[i];for(int i=0;i<n;i++)cin>>b[i];sort(all(a));sort(all(b));
		int ans1=0,ans2=0;x=a;y=b;reverse(all(y));
		for(int i=0;i<n;i++){
			for(int j=0;j<y.size();j++){
				if(y[j]<x[i]){ans1++;y.erase(y.begin()+j);break;}
			}
		}
		for(int i=0;i<n;i++){
			bool check=true;
			for(int j=0;j<b.size();j++){
				if(b[j]>a[i]){check=false;b.erase(b.begin()+j);break;}
			}
			if(check)ans2++;
		}
		cout<<"Case #"<<++cs<<": "<<ans1<<" "<<ans2<<endl;
	}
	return 0;
}
