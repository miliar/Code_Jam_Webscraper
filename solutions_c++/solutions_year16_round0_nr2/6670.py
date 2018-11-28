//-------------------------------
#include<bits/stdc++.h>
using namespace std ;
//-------------------------------
typedef long long ll ;
typedef vector<int> vi ;
typedef pair<int,int> ii ;
//-------------------------------
 
#define pb(a) push_back(a)
#define mp(a,b) make_pair(a,b)
#define rep(i,a,b) for(int i=(a) ; i<(b) ; ++i)
#define inf 2000000000
#define endl "\n"
#define max(a,b) ( (a>b) ? (a) : (b)  )
#define min(a,b) ( (a<b) ? (a) : (b)  )
//------------------------------
int ri()
{
	char c = getchar() ;
	while(c<'0' || c>'9') c = getchar() ;
	int ret = 0 ;
	while(c>='0' && c<='9')
	{
		ret = 10*ret+c-48;
		c = getchar();
	}
	return ret;
}

char s[110];
int L=0;
int K=1;
int T;
void ok(int x)
{
	for(int j=x;j>=0;--j)
		if(s[j]=='-')
			s[j]='+';
		else
			s[j]='-';
}

int main()
{

	freopen("bb.in","r",stdin);
	freopen("out.txt","w",stdout);

	T=ri();
	while(T--)
	{
		scanf("%s",s);
		L=strlen(s);
		int cnt=0;
		for(int i=L-1;i>=0;--i)
			if(s[i]=='-')
			{
				cnt++;
				ok(i);
			}
		printf("Case #%d: %d\n",K++,cnt);
	}
}

