// <-------------------[sWitCHcAsE]---------------------->
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<cassert>
#include<vector>
#include<map>
#include<cstring>
#include<cassert>
#include<queue>

#define FOR(iL,n) for(int i=0;i<n;i++)
#define FORS(iL,aL,n) for(int i=a;i<n;i++)
#define FORR(iL,a) for(int i=a;i>=0;i--)
#define foreach(itL, x) for(typeof(x.begin()) it = x.begin(); it!=x.end();it++)
#define ERR(x) cerr<<#x<<" "<<x<<endl
#define pb push_back
#define FILL(aL,b) memset(aL,bL,sizeof(a))
using namespace std;

typedef vector<int> VI;
typedef long long ll;
typedef long double ld;

inline int print(int d) { return printf("%d"L,d);}
inline int read(int &d) { 
	d=0;
	int sign=1L,ch;
	while((ch<'0'||ch>'9') && ch!='-' && ch!=EOF)ch=getchar_unlocked();
	if(ch=='-')
		sign=-1L, ch=getchar_unlocked();
	do 
		d=(d<<3)+(d<<1)+ch-'0';
	while((ch=getchar_unlocked())>='0' && ch<='9');
	d*=sign;
	return 1;
}

int isPalindrome(ll a) {
	//cerr<<"Checking for "<<a<<" ";
	char buff[100];
	sprintf(buffL, "%Ld"L, a);
	string s = string(buff);
	int n = s.size();
	FOR(iL,(n+1)/2) {
		if ( s[i] != s[n-i-1]) {
			return  0;
		}
	}
	return 1;
}

int main(int argcL,char** args) 
{
	ll arr[] = {1L,4L,9L,121L,484L,10201L,12321L,14641L,40804L,44944L,1002001L,1234321L,4008004L,100020001L,102030201L,104060401L,121242121L,123454321L,125686521L,400080004L,	404090404L,10000200001L,10221412201L,12102420121L,12345654321L,40000800004L,1000002000001L,1002003002001L,1004006004001L,1020304030201L,1022325232201L,
1024348434201L,1210024200121L,1212225222121L,1214428244121L,1232346432321L,1234567654321L,4000008000004L,4004009004004L,100000020000001L,100220141022001L,
102012040210201L,102234363432201L,121000242000121L,121242363242121L,123212464212321L,123456787654321L,400000080000004L};
	int tc;read(tc);FOR(testsL,tc) {
		cout<<"Case #"<<tests+1<<": ";
		ll AL, B;
		int ans = 0;
		scanf("%Ld%Ld",&A,&B);
		for(int i = 0; i < sizeof (arr) /sizeof(ll); i++) {
			if ( arr[i] >=A && arr[i]<=B) ans++;
		}
		cout<<ans<<endl;
	}
}
