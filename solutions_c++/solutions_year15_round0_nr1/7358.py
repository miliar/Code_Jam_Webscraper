#include<bits/stdc++.h>

using namespace std;
 
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
 
#define GI ({int t;scanf("%d",&t);t;})
#define REP(i,a,b) for(int i=a;i<b;i++)
#define ALL(v) (v).begin(),(v).end()
#define TR(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define pb push_back
#define mp make_pair
#define INF (int)1e9
#define EPS (double)(1e-9)
#define PI (double)(3.141592653589793)
#define gc getchar
#define ff first
#define ss second

inline int read(){
int n = 0, c = gc(), f = 1;
while(c != '-' && (c < '0' || c > '9')) c = gc();
if(c == '-') f = -1, c = gc();
while(c >= '0' && c <= '9')
n = (n<<3) + (n<<1) + c - '0', c = gc();
return n * f;
}
 
int main()
{
	
	int t;
	int s,rr,i;
	string str;
	long cnt,shy;
	
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	scanf("%d",&t);
	rr=1;
	while(t--)		{
		
	cin >> s;
	cin >> str;	
	cnt=0;shy=0;	
	for(i=0;i<str.size();i++)	{
	
		if(str[i]!='0')	{
		if(cnt<i)	{
			shy+=i-cnt;
			cnt=i;
		} 
		cnt+=str[i]-'0';		
	  }
    }
	printf("Case #%d: %ld\n",rr++,shy);	
	}  
    
return 0;
}
