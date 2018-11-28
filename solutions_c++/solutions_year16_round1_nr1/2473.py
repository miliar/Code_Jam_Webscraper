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

char s[3000],final[3000];
int mid  ;

int main(int argc, char const *argv[])
{
	int t;
	sc1(t);
	mid = 1500;
	int temp = t;
	while(t--)
	{
		int i,low = 1500,high =1500;
		scanf("%s",s);
		final[low] = s[0];
		for(i= 1;s[i];++i)
		{
			if(s[i]>=final[low])
			{
				final[--low] = s[i];
			}
			else
			{
				final[++high] = s[i];
			}
		}
		printf("Case #%d: ",temp-t);
		for(i = low;i<=high;++i)
		{
			printf("%c",final[i]);
		}
		printf("\n");
	}
	
	return 0;
}