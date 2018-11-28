/*Author : Vineet Kumar */
#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<climits>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<bitset>
#include<stack>
#include<queue>
#include<fstream>
using namespace std;
 
#define FOR(i,a,b) 	for(int i= (int )a ; i < (int )b ; ++i)
#define rep(i,n) 	FOR(i,0,n)
#define INF		INT_MAX
#define ALL(x) 		x.begin(),x.end()
#define LET(x,a)	__typeof(a) x(a)
#define IFOR(i,a,b) 	for(LET(i,a);i!=(b);++i)
#define EACH(it,v) 	IFOR(it,v.begin(),v.end())
#define pb 		push_back
#define sz(x) 		int(x.size())
#define mp 		make_pair
#define fill(x,v)	memset(x,v,sizeof(x))
#define max(a,b)	((a)>(b)?(a):(b))
#define min(a,b)	((a)<(b)?(a):(b))
#define	si(n)		scanf("%d",&n)
#define pi(n)		printf("%d ",n)
#define pil(n)		printf("%d\n",n)
#define ps(n)		printf("%s",n)
#define psl(n)		printf("%s\n",n)
#define sl(n)		scanf("%lld",&n)
#define sd(n)		scanf("%lf",&n)
#define ss(n)		scanf("%s",n)
#define scan(v,n)	vector<int> v;rep(i,n){ int j;si(j);v.pb(j);}
#define scan_in(v,n)	vector<int> v;rep(i,n){ int j;in>>j;v.pb(j);}
#define scan_in_s(v,n)	vector<string> v;rep(i,n){ string j;in>>j;v.pb(j);}
#define mod (int)(1e9 + 7)
typedef pair<int,int> PI;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

int main()
{
	int T;
	
	ifstream in("LawnMower.txt");
	ofstream out("LawnMower_out.txt");
	
	in>>T;// = atoi(str);
	vector<string> s;
	int r = T;
	
	while(T--)
	{
		int N,M;
		in>>N>>M;
		int array[N][M];
		rep(i,N)
		{
			rep(j,M)
			{
				in>>array[i][j];
			}
		}
		bool can = true;
		rep(i,N)
		{
			rep(j,M)
			{
				bool comp = true;
				rep(k,M)
				{
					if(array[i][k]>array[i][j])
					{
						comp = false;
						break;
					}
				}
				if(comp==false)
				{
					comp = true;
					rep(k,N)
					{
						if(array[k][j]>array[i][j])
						{
							comp = false;
							break;
						}
					}
				}
				if(comp==false)
				{
					can = false;
					break;
				}
				
				//array[i][j];
			}
			if(can==false)break;
			
		}
		//output init..
		char buffer[50];
		sprintf(buffer,"Case #%d: ",r-T);
		out<<buffer;
		//output
		if(can==true)out<<"YES"<<endl;
		else out<<"NO"<<endl;
	}
	
	in.close();
	out.close();
	
	return 0;
}

