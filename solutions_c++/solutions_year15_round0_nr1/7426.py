#include <bits/stdc++.h>
using namespace std;

typedef	long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int, int> pii;
#define pb push_back
#define mp make_pair
#define rep(i,n) for(int i = 0; i < n; i++)
#define sc(n) scanf("%d",&n)
#define scll(n) scanf("%I64d",&n)
#define mod 1000000007
#define ll long long
template<class T>inline T gcd(T a,T b){return b?gcd(b,a%b):a;}
int main()
{
	freopen("input1.txt","r",stdin);
	freopen("output1.txt","w",stdout);
	int test;
	sc(test);
	for(int t = 1; t <= test; t++){
		int m;
		sc(m);
		string str;
		cin>>str;
		int ans = 0;
		int cnt = 0;
		for(int i = 0;i<str.length();i++){
			if(str[i]!='0'){
				if(cnt<i){
					ans += i-cnt;
					cnt = i;
				}
				cnt += (str[i]-'0');
			}
		}
		printf("Case #%d: %d\n",t,ans);
	}
}

