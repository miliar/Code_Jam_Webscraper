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
#define ui unsigned int


unsigned int cur =0;
unsigned int func()
{
	unsigned int v; // current permutation of bits
	v = cur;
	unsigned int w; // next permutation of bits

	unsigned int t = v | (v - 1); // t gets v's least significant 0 bits set to 1
	// Next set to 1 the most significant bit to change,
	// set to 0 the least significant ones, and add the necessary 1 bits.
	w = (t + 1) | (((~t & -~t) - 1) >> (__builtin_ctz(v) + 1));
	return w;
}

vector<int > v[50];

int main(int argc, char const *argv[])
{
	int t,temp;
	sc1(t);
	temp = t;
	while(t--)
	{

		cur = 0;
		int n,i,j;
		sc1(n);
		for(i=0;i<2*n;++i)
		{
			v[i].clear();
		}
		for(i=0;i<2*n-1;++i)
		{
			for( j =0;j<n;++j)
			{
				int x;
				sc1(x);

				v[i].pb(x);
			}

		}
		
		for(i=0;i<n;++i)
		{
			cur|=(1<<i);
		}
		ui lim =0;;
		for(i=2*n-2;i>=n-1;--i)
		{
			lim|=(1<<i);
		}
		int flagfinal = 0;
		vector<int> store;

		

		while(cur<=lim)
		{
			bool vis[25]={0};
			vector<int> hello [n+1];
			vector<pii > ss;
			ui temp = cur;
			int c  = 0;
			while(temp>0)
			{
				if(temp&1)
				{
					ss.pb(mp(v[c][0],c));
				}
				temp/=2;
				c++;
			}
		//	printf("hi\n");
			sort(all(ss));

			for( i =0;i<ss.size();++i)
			{
				hello[i] = v[ss[i].sc];
				vis[ss[i].sc ]=1;
			/*	for(j=0;j<hello[i].size();++j)
				{
					printf("%d ",hello[i][j]);
				}
				printf("\n");*/
			}
			/*printf("\n-------------\n");*/

			vector<int> misc;
			store.clear();
			int check=0;
			
			for(i=0;i<n;++i)
			{
				misc.clear();
				for(j=0;j<n;++j)
				{
					misc.pb(hello[j][i]);
				}
				/*printf("misc :: \n");
				for(j = 0;j<misc.size();++j)
				{
					printf("%d ",misc[j]);
				}
				printf("\n");*/
				int f=0;
				for(j = 0;j<2*n-1;++j)
				{
					if(!vis[j])
					{
						if(misc == v[j])
						{
							f = 1;
							vis[j]  = 1;
							break;
						}
					}
				}
				if(check>1)
					break;
				if(f==0)
				{
					check++;
					store = misc;
				}
			}
			if(check==1)
			{
				flagfinal = 1;
				break;
			}
		//	debug(check);
			cur = func();

		}
				printf("Case #%d: ",temp-t);
			for(i = 0;i<store.size();++i)
			{
				printf("%d ",store[i]);
			}
			printf("\n");
	



				


	}
	
	return 0;
}