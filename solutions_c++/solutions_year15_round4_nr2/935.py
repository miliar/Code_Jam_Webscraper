#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

typedef unsigned long long ull;
typedef pair<ll,ll> ii;
typedef vector<ll> vi;
typedef vector< ii > vii;

#define INF 0x3F3F3F3F
#define LINF 0x3F3F3F3F3F3F3F3FLL
#define pb push_back
#define mp make_pair
#define pq priority_queue
#define LSONE(s) ((s)&(-s)) //LASTBIT
#define DEG_to_RAD(X)   (X * PI / 180)
#define F first
#define S second

 
#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) fprintf(stderr,args)
#endif

//////////////////////
int dx[] = {1,-1,0,0};
int dy[] = {0,0,-1,1};	
//////////////////////

#define EPS 1e-10

using namespace std;

int n,m;
char M[110][110];
long double w[200][2];

void main2()
{
	int n;
	long double v,x;
	scanf("%d %Lf %Lf",&n,&v,&x);
	for(int i = 0;i<n;i++) scanf("%Lf %Lf",&w[i][0],&w[i][1]);
	if(n == 2 && fabs(w[0][1]-w[1][1])<EPS )
	{
		n = 1;
		w[0][0] = w[0][0]+w[1][0];
	}
	if(n == 2 && fabs(w[0][1]-x)<EPS) n = 1;
	if(n == 2 && fabs(w[1][1]-x)<EPS)
	{
		n = 1;
		w[0][0] = w[1][0];
		w[0][1] = w[1][1];
	}

	if((w[0][1]>x && w[1][1]>x) || (w[0][1]<x && w[1][1]<x))
	{
		puts("IMPOSSIBLE");
		return;
	}

	if(n == 1)
	{
		if((w[0][1]>x ) || (w[0][1]<x))
		{
			puts("IMPOSSIBLE");
			return;
		}
		printf("%.9Lf\n",v/w[0][0]);
		return;
	}

	if(w[0][1]<w[1][1])
	{
		swap(w[0][0],w[1][0]);
		swap(w[0][1],w[1][1]);
	}

	long double razao = (x - w[1][1])/(w[0][1] - x);
	long double v0 = (v*razao)/(razao+1.0);
	long double v1 = (v)/(razao+1.0);
	long double s = max(v0/w[0][0],v1/w[1][0]);
	printf("%.9Lf\n",s);
}

int main()
{
	int t,ca = 1;
	scanf("%d",&t);
	while(t--)
	{
		printf("Case #%d: ",ca++);
		main2();
	}
	return 0;
}