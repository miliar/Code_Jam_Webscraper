#include<cstdio>
#include<set>
using namespace std;
struct node{ int i,v; };
struct comp{ bool operator()(node x,node y){ if( x.v<y.v ) return true; if( x.v==y.v && x.i<y.i ) return true; return false; } };
int b[1000];
int main()
{
int N;
scanf("%d",&N);
for(int T=1;T<=N;T++)
{
	int n,m;
	scanf("%d",&n);
	set<node,comp> h;
	for(int a=0;a<n;a++){ int t; scanf("%d",&t); h.insert((node){a,t}); }
	for(int a=0;a<n;a++)
	{
		node nt=*h.begin(); h.erase(nt);
		b[nt.i]=a;
	}
	int c=0;
	int p=0,q=n-1;
	for(int a=0;a<n;a++)
	{
		int s;
		for(s=p;s<=q;s++)
		{
			if( b[s]==a ) break;
		}
		if( s-p<=q-s )
		{
			for(int d=s;d>p;d--)
			{
				b[d]=b[d-1];
				c++;
			}
			b[p]=b[s];
			p++;
		}
		else
		{
			for(int d=s;d<q;d++)
			{
				b[d]=b[d+1];
				c++;
			}
			b[q]=b[s];
			q--;
		}
	}
	printf("Case #%d: ",T);
	printf("%d",c);
done:;
	printf("\n");
}
	return 0;
}
