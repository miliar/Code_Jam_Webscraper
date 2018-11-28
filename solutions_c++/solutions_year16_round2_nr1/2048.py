#include<bits/stdc++.h>
#define f(i,a,n) for(int i=a;i<n;i++)
#define S second
#define F first
#define Sc(n) scanf("%lld",&n)
#define scc(a,b,c) scanf("%lld %lld %lld",&a,&b,&c)
#define sp(a) scanf("%lld %lld",&a.first,&a.second)
#define pb push_back
#define mp make_pair
#define lb lower_bound
#define ub upper_bound
#define all(a) a.begin(),a.end()
#define sc(n) scanf("%d",&n)
#define It iterator
#define SET(a,b) memset(a,b,sizeof(a))
#define DRT()  int t,t1=0; cin>>t; while(t1++<t)
// inbuilt functions
// __gcd,  __builtin_ffs,     (returns least significant 1-bit, __builtin_ffsll(1)=1)
// __builtin_clz,             (returns number of leading zeroes in 
// __builtin_popcount,
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> vi;
#define tr(container, it) for(__typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define trv(s,it) for(auto it:s)
char s[2005],cmp[][9]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int k[]={4,3,3,5,4,4,3,5,5,4};
int cnt[12],cn[30];
int main()
{	DRT()
	{	cin>>s;
		int n=strlen(s);
		int j=0;
		SET(cnt,0);
		SET(cn,0);
		f(i,0,n)
			cn[s[i]-'A']++;
//		f(i,0,26)
//			cout<<cn[i]<<" ";
		while(cn[25]--)
		{	cnt[0]++;
			cn[4]--;
			cn['R'-'A']--;
			cn['O'-'A']--;
		}
		while(cn[22]--)
		{	cnt[2]++;
			cn['T'-'A']--;
			cn['O'-'A']--;
		}
		while(cn[20]--)
		{	cnt[4]++;
			cn[5]--;
			cn[17]--;
			cn[14]--;
		}
		while(cn[14]--)
		{	cnt[1]++;
			cn[13]--;
			cn[4]--;
		}
		while(cn[23]--)
		{	cnt[6]++;
			cn[18]--;
			cn[8]--;
		}
		while(cn[5]--)
		{	cnt[5]++;
			cn[21]--;
			cn[8]--;
			cn[4]--;
		}
		while(cn[21]--)
		{	cnt[7]++;
			cn[18]--;
			cn[4]-=2;
			cn[13]--;
		}
		cnt[9]=cn[13]/2;
		while(cn[6]--)
		{	cnt[8]++;
			cn[4]--;
			cn[7]--;
			cn[8]--;
			cn[19]--;
		}
		cnt[3]=cn[19];
		printf("Case #%d: ",t1);
		f(i,0,10)
			while(cnt[i]--)
				printf("%c",'0'+i);
		cout<<endl;
	}
}


