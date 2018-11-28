#include<iostream>
#include<stdio.h>
#include<functional>
#include<algorithm>
#include<math.h>
#include<limits.h>

#include<set>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<deque>

#include<cstring>
#include<string>


#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define pb push_back 
#define lli long long int
#define mod1 1000000007
#define mod2 1000000009
#define ppi pair<int,int>
#define tr(a,it) for(typeof(a.begin()) it=a.begin();it!=a.end();it++)

using namespace std;

int main() {
	
	int t;
	cin>>t;
	FOR(j,0,t-1)
	{
		int n;
		cin>>n;
		n++;
		int a[n];
		char x;
		FOR(i,0,n-1)
		{
			cin>>x;
			a[i]=x-'0';
		}
		
		int sf=a[0],ans=0,curr=1;
		FOR(i,1,n-1)
		{
		
			if (sf>=i){
				sf+=a[i];
			}
			else
			{
				ans+=i-sf;
				sf= i+a[i];
			}
		}
		cout<<"Case #"<<j+1<<": "<<ans<<endl;
	}
	return 0;
}
