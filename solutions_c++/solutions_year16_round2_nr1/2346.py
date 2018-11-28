//Satyam Pandey :: Kamehameha //
#include<bits/stdc++.h>

using namespace std;

typedef pair<int,int> II;
typedef vector<II> VII;
typedef vector<int> VI;
typedef vector< VI > VVI;
typedef long long int LL;

#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(a) (int)(a.size())
#define ALL(a) a.begin(),a.end()
#define SET(a,b) memset(a,b,sizeof(a))

#define si(n) scanf("%d",&n)
#define dout(n) printf("%d\n",n)
#define sll(n) scanf("%lld",&n)
#define lldout(n) printf("%lld\n",n)
#define fast_io ios_base::sync_with_stdio(false);cin.tie(NULL)

#define TRACE

#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
  cerr<<name<<" : "<<arg1<<endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names,Arg1&& arg1,Args&&... args){
  const char* comma=strchr(names+1,',');
  cerr.write(names,comma-names)<<" : "<<arg1<<" | ";__f(comma+1,args...);
}
#else
#define trace(...)
#endif

//FILE *fin = freopen("in","r",stdin);
//FILE *fout = freopen("out","w",stdout);
int CNT[30];
int ANS[20];
char s[5000];
int main()
{
	int t,tt;si(t);
	for(tt=1;tt<=t;tt++)
	{
		int i,j;
		scanf("%s",s);
		SET(CNT,0);SET(ANS,0);
		for(i=0;s[i]!='\0';i++)
			CNT[s[i]-'A']++;
		ANS[0]=CNT['Z'-'A'];
		CNT['E'-'A']-=CNT['Z'-'A'];
		CNT['R'-'A']-=CNT['Z'-'A'];
		CNT['O'-'A']-=CNT['Z'-'A'];
		CNT['Z'-'A']-=CNT['Z'-'A'];
		ANS[2]=CNT['W'-'A'];
		CNT['T'-'A']-=CNT['W'-'A'];
		CNT['O'-'A']-=CNT['W'-'A'];
		CNT['W'-'A']-=CNT['W'-'A'];
		ANS[4]=CNT['U'-'A'];
		CNT['F'-'A']-=CNT['U'-'A'];
		CNT['O'-'A']-=CNT['U'-'A'];
		CNT['R'-'A']-=CNT['U'-'A'];
		CNT['U'-'A']-=CNT['U'-'A'];
		ANS[6]=CNT['X'-'A'];
		CNT['S'-'A']-=CNT['X'-'A'];
		CNT['I'-'A']-=CNT['X'-'A'];
		CNT['X'-'A']-=CNT['X'-'A'];
		ANS[3]=CNT['R'-'A'];
		CNT['T'-'A']-=CNT['R'-'A'];
		CNT['H'-'A']-=CNT['R'-'A'];
		CNT['E'-'A']-=CNT['R'-'A'];
		CNT['E'-'A']-=CNT['R'-'A'];
		CNT['R'-'A']-=CNT['R'-'A'];
		ANS[8]=CNT['H'-'A'];
		CNT['E'-'A']-=CNT['H'-'A'];
		CNT['I'-'A']-=CNT['H'-'A'];
		CNT['G'-'A']-=CNT['H'-'A'];
		CNT['T'-'A']-=CNT['H'-'A'];
		CNT['H'-'A']-=CNT['H'-'A'];
		ANS[1]=CNT['O'-'A'];
		CNT['N'-'A']-=CNT['O'-'A'];
		CNT['E'-'A']-=CNT['O'-'A'];
		CNT['O'-'A']-=CNT['O'-'A'];
		ANS[7]=CNT['S'-'A'];
		CNT['N'-'A']-=CNT['S'-'A'];
		CNT['E'-'A']-=CNT['S'-'A'];
		CNT['V'-'A']-=CNT['S'-'A'];
		CNT['E'-'A']-=CNT['S'-'A'];
		CNT['S'-'A']-=CNT['S'-'A'];
		ANS[5]=CNT['F'-'A'];
		CNT['E'-'A']-=CNT['F'-'A'];
		CNT['V'-'A']-=CNT['F'-'A'];
		CNT['I'-'A']-=CNT['F'-'A'];
		CNT['F'-'A']-=CNT['F'-'A'];
		ANS[9]=CNT['I'-'A'];
		CNT['E'-'A']-=CNT['I'-'A'];
		CNT['N'-'A']-=CNT['I'-'A'];
		CNT['N'-'A']-=CNT['I'-'A'];
		CNT['I'-'A']-=CNT['I'-'A'];
		printf("Case #%d: ",tt);
		for(i=0;i<10;i++)
		{
			for(j=0;j<ANS[i];j++)
				printf("%d",i);
		}
		printf("\n");
	}
	return 0;
}
