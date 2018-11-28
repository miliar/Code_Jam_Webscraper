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
int a[10]={0};
bool ok()
{
	int cnt=0;
	rep(i,0,10)
		if(a[i]) cnt++;
	return cnt==10;
}
int T;
ll n;
int K=1;
int main()
{

	freopen("aa.in","r",stdin);
	freopen("out.txt","w",stdout);

	T=ri();
	while(T--)
	{
		memset(a,0,sizeof a);
		n=ri();
		if(n)
		{
			ll j=1LL,te=0,ra=0;
			while(!ok())
			{
				//n = n*j;
				te=n*j;
				ra=te;
				while(te)
				{
					int rem=te%10;
					a[rem]=1;
					te/=10;
				}
				++j;
				//cout << ra << endl;
			}

			printf("Case #%d: %lld\n",K++,ra);
		}
		else
			printf("Case #%d: INSOMNIA\n",K++);
	}
}
