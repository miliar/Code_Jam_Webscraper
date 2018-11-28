#include <iostream>
#include <sstream>
#include <ios>
#include <iomanip>
#include <functional>
#include <algorithm>
#include <vector>
#include <string>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <climits>
using namespace std;
#define XINF INT_MAX
#define INF 0x3FFFFFFF
#define MP(X,Y) make_pair(X,Y)
#define PB(X) push_back(X)
#define REP(X,N) for(int X=0;X<N;X++)
#define REP2(X,L,R) for(int X=L;X<=R;X++)
#define IT iterator
typedef long long ll;
typedef pair<int,int> PII;
typedef vector<PII> VII;
typedef vector<int> VI;

int main()
{
	ios::sync_with_stdio(false);
	freopen("A-small-attempt0.in","r+",stdin);
	freopen("A-small-attempt0.out","w+",stdout);
	int t,cs=1;
	cin>>t;
	while(t--)
	{
		int n,x;
		int a[4], b[4];
		cin>>n;
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				cin>>x;
				if(i==n-1)
				{
					a[j]=x;
				}
			}
		}
		
		cin>>n;
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				cin>>x;
				if(i==n-1)
				{
					b[j]=x;
				}
			}
		}
		
		int c=0, ans;
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				if(a[i]==b[j])
				{
					c++;
					ans=a[i];
				}
			}
		}
		
		cout<<"Case #"<<cs++<<": ";
		if(c==0)
		{
			cout<<"Volunteer cheated!";
		}else if(c>1){
			cout<<"Bad magician!";
		}else{
			cout<<ans;
		}
		cout<<endl;
	}
	return 0;
}

