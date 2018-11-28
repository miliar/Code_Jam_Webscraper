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
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int t,cs=0;cin>>t;
	while(t--){
		vector<int> v(20,0);
		int n,x;cin>>n;
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				cin>>x;
				if(i==n)v[x]=1;
			}
		}
		int cnt=0,ans=0;cin>>n;
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				cin>>x;
				if(i==n){
					if(v[x]==1)ans=x,cnt++;
				}
			}
		}
		cout<<"Case #"<<++cs<<": ";
		if(cnt==1)cout<<ans<<endl;
		else if(cnt>1)cout<<"Bad magician!"<<endl;
		else if(cnt==0)cout<<"Volunteer cheated!"<<endl;
	}
	return 0;
}
