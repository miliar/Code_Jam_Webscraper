#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef complex<double> cplx;

#define sqr(x) ((x)*(x))
#define pb push_back
#define X first
#define Y second
#define sit(a) set<a>::iterator
#define mit(a,b) map<a,b>::iterator

const ll mod=1000000007LL;
const int inf=0x3f3f3f3f;
const int maxn=100005,maxm=1005;
const double eps=1e-10;
const double pi=acos(-1.0);

int T;
char c[maxn];
int n;
string re;

int main()
{
        freopen("in.txt","r",stdin);
        freopen("out.txt","w",stdout);
	int i,j,I;
	scanf("%d",&T);
	for(I=1;I<=T;I++)
	{
		printf("Case #%d: ",I);
		scanf("%s",c);
		n=strlen(c);re="";
		re+=c[0];
		for(i=1;i<n;i++)
		{
			re=max(re+c[i],c[i]+re);
		}
		cout<<re<<"\n";
		cerr<<I<<endl;
	}
        return 0;
}
