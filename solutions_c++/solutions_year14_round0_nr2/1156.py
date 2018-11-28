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
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t,cs=0;cin>>t;
	while(t--){
		double c,f,x,rate=2.0;cin>>c>>f>>x;
		double prev=0.0,sum=0.0,ans=0.0;bool check=true;
		while(true){
			ans=sum+(x/rate);
			sum+=(c/rate);rate+=f;
			if(check){check=false;prev=ans;continue;}
			if(ans>prev){ans=prev;break;}
			prev=ans;
		}
		cout<<"Case #"<<++cs<<": ";
		cout<<fixed<<setprecision(7)<<ans<<endl;
	}
	return 0;
}
