#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <complex>
#include <string>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <queue>
#include <stack>
#include <functional>
#include <iostream>
#include <map>
#include <set>
using namespace std;
typedef pair<int,int> P;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
#define pu push
#define pb push_back
#define mp make_pair
#define eps 1e-9
#define INF 2000000000
#define sz(x) ((int)(x).size())
#define fi first
#define sec second
#define SORT(x) sort((x).begin(),(x).end())
#define all(x) (x).begin(),(x).end()
#define rep(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define repn(i,a,n) for(int (i)=(a);(i)<(int)(n);(i)++)
#define EQ(a,b) (abs((a)-(b))<eps)
int T;
int num[1010];
int main()
{
	cin >> T;
	for(int t=0;t<T;t++)
	{
		memset(num,0,sizeof(num));
		string s;
		int S;
		cin >> S >> s;
		for(int i=0;i<=S;i++)num[i]=(s[i]-'0');
		int ans = 0,sum = num[0];
		for(int i=1;i<=S;i++)
		{
			if(num[i]==0)continue;
			if(sum<i)
			{
				ans += i-sum;
				sum = i;
			}
			sum += num[i];
		}
		printf("Case #%d: %d\n",t+1,ans);
	}
	return 0;
}
