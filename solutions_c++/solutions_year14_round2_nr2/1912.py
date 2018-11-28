#include<map>
#include<set>
#include<ctime>
#include<cmath>
#include<queue>
#include<stack>
#include<bitset>
#include<vector>
#include<cstdio>
#include<string>
#include<cassert>
#include<cstring>
#include<numeric>
#include<sstream>
#include<iterator>
#include<iostream>
#include<algorithm>

using namespace std;
typedef unsigned long long LL;

#define MOD7 1000000007
#define MOD9 1000000009

#define pb push_back
#define mp make_pair


#define MM(a,x) memset(a, x, sizeof(a))
#define P(x) cout<<#x<<" = "<<x<<endl;
#define P2(x,y) cout<<#x<<" = "<<x<<", "<<#y<<" = "<<y<<endl;
#define PV(a,n) for(int i=0;i<n;i++) cout<<#a<<"[" << i <<"] = "<<a[i]<<endl;
#define TM(a,b) cout<<#a<<"->"<<#b<<": "<<1.*(b-a)/CLOCKS_PER_SEC<<"s\n";

#define all(X) (X).begin(), (X).end ()
#define for_each(it, X) for (__typeof((X).begin()) it = (X).begin(); it != (X).end(); it++)


int main()
{
    cin.sync_with_stdio ( 0 );
    cout.sync_with_stdio ( 0 );
	int T=1;
	cin>>T;
	for(int p =1 ; p <=T ; p++)
	{
			int a,b,k;
			int count = 0;
			cin>>a>>b>>k;
			int i,j;
			for(i=0 ; i< a ; i++)
			{
				for(j=0  ; j< b ; j++)
				{
					if(( i&j) < k)
						count++;
				}
			}
			cout<<"Case #"<<p<<": "<<count<<endl;
	}
	return 0;
}
