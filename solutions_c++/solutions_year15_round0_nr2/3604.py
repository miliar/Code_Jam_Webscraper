#include <bits/stdc++.h>
#include <time.h>
#include <stdlib.h>
using namespace std;
//defines-general
typedef long long ll;
typedef long double ld;
#define to(a) __typeof(a)
#define fill(a,val) memset(a,val,sizeof(a))
#define repi(i,a,b) for(__typeof((b)) i = a;i<(b);i++)
//defines-pair
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
#define ff first
#define ss second
#define mp make_pair
//defines-vector
typedef vector<int> vi;
typedef vector<long long> vll;
#define all(vec) vec.begin(),vec.end()
#define tr(vec,it) for(__typeof(vec.begin()) it = vec.begin();it!=vec.end();++it)
#define tr2(vec,it,itb) for(__typeof(vec.begin()) it = itb;it!=vec.end();++it)
#define pb push_back
#define sz size()
#define contains(vec,x) (find(vec.begin(),vec.end(),x)!=vec.end())

#define MOD 1000000007
bool compareF(int a, int b)
{
	if(a<b)
		return false;
	return true;
}
int main()
{
	std::ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for(int i = 1; i<=t;i++)
	{
		int d;
		cin >> d;
		int nums[d+1];
		
		for(int j=0;j<d;j++)
			cin >> nums[j];
		
		
		int mn = 1001;
		int m_1;
		for(int m = 1; m<1001; m++)
		{
			int special = 0;
			for(int j=0; j<d;j++)
				if(nums[j]>m)
					special+=ceil((nums[j]*1.0)/(m*1.0)) -1 ;

			if(mn>(m+special))
			{
				mn = m+special;
				m_1 = m;
			}
		}
		cout <<"Case #"<<i<<": "<<mn<<endl;
	}
	return 0;
}