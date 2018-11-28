#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<queue>
#include<map>
#include<set>
#include<string>
#include<sstream>
#include<climits>
#include<vector>
#include<cstring>
#include<stack>

using namespace std;

#define all(c) (c).begin(),(c).end()
#define vi vector<int>
#define vvii vector< vi >
#define REP(i,s,n)  for (int i=(s),_n=(n);i<=_n;i++)
#define FOR(i,s,n)  for (int i=(s),_n=(n);i<_n;i++)
#define REPD(i,e,s)  for (int i=(e),_s=(s);i>=_s;i--)
#define tr(container, it) \
	for (typeof(container.begin()) it=container.begin(); it!=container.end();it++)
#define ALL(x) x.begin(),x.end()
#define debug(args...)	{dbg,args; cerr<<endl;}
#define PB push_back
#define MP make_pair
#define EPS 1e-8
#define INF (int)(1e9)
typedef long long LL;

struct debugger {
	template<typename T> debugger& operator , (const T& v) {	
		cerr<<v<<" ";	
		return *this;	
	}
} dbg;


int main() {
	int T,ind=1;
	cin >> T;
	while(T--)
	{
		int r,temp;
		cin >> r;
		vi pr1,pr2;
		FOR(i,0,4)
		{
			FOR(j,0,4)
			{
				if(i+1==r)
				{
					cin >> temp;
					pr1.PB(temp);
				}
				else

					cin >> temp;

			}
		}
		cin >> r;
		FOR(i,0,4)
		{
			FOR(j,0,4)
			{
				if(i+1==r)
				{
					cin >> temp;
					pr2.PB(temp);
				}
				else

					cin >> temp;

			}
		}
		vi ans;
		FOR(i,0,4)
		{
			FOR(j,0,4)
			{
				if(pr1[i]==pr2[j])
				{
					ans.PB(pr1[i]);
				}
			}
		}
		if(ans.size()==1)
			cout << "Case #"<< ind<<": "<<ans[0]<<"\n";
		else if(ans.empty()==1)
			cout << "Case #"<<ind <<": Volunteer cheated!\n";
		else
			cout << "Case #"<<ind<<": Bad magician!\n";
		ind++;

	}
	return 0;
}

