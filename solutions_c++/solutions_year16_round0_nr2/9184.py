#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int > pii;
typedef pair<int,pii > piii;
//input
#define sc1(x) scanf("%d",&x);
#define sc2(x,y) scanf("%d%d",&x,&y);
#define sc3(x,y,z) scanf("%d%d%d",&x,&y,&z);

/*
#define sc1(x) scanf("%lld",&x);
#define sc2(x,y) scanf("%lld%lld",&x,&y);
#define sc3(x,y,z) scanf("%lld%lld%lld",&x,&y,&z);
*/

#define pb push_back
#define mp make_pair
#define ini(x,val) memset(x,val,sizeof(x));

#define fs first
#define sc second

//some constants
#define MOD 1000000007
#define inf 99999999
#define linf 99999999999999999ll	//long long inf
#define PI 3.1415926535897932384626
const double eps=0.000000000000001 ;

#define gcd __gcd
#define tr(container, it)  for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
#define all(v) v.begin(),v.end()

#define debug(x) cout<<#x<<" :: "<<x<<"\n";
#define debug2(x,y) cout<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\n";
#define debug3(x,y,z) cout<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\t"<<#z<<" :: "<<z<<"\n";

#define LIM 100005

char s[105];
vector<int> a;

void flip(int ind1,int ind2)
{
	for(int i = ind1;i<=ind2;++i)
	{
		a[i]^=1;
	}
}

int main(int argc, char const *argv[])
{
	int t,i,ans,temp;
	sc1(t);
	temp = t;
	while(t--)
	{
		ans = 0;
		a.clear();
		scanf("%s",s);
		for(i=0;s[i];++i)
		{
			if(s[i] == '+')
			{
				a.pb(1) ;
			}
			else a.pb(0);
		}
		int len = strlen(s);
		/*for(int j = 0;j<a.size();++j)
			{
				printf("%d",a[j]);
			}
			printf("\n");*/
		for(i = a.size()-1; i>=0;--i)
		{
			if(a[i] == 0)
			{
				if(a[0] == 0)
				{
					++ans;
					flip(0,i);
					reverse(a.begin(),a.begin()+i+1);
					
				}
				else
				{
					ans+=2;
					for(int j = 0;j<a.size();++j)
					{
						if(a[j]==0)
							break;
						flip(j,j);
					}
					
					flip(0,i);
					reverse(a.begin(),a.begin()+i+1);


				}
			}/*
			for(int j = 0;j<a.size();++j)
			{
				printf("%d",a[j]);
			}
			printf("\n");*/
		}
		printf("Case #%d: %d\n",temp-t,ans);

	}
	
	return 0;
}