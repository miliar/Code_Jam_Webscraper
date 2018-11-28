#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;
typedef unsigned char byte;

class Int
{
	private:
		int l;
		byte d[101];
	public:
		void operator=(const char *buf)
		{
			while(*buf=='0')buf++;
			l=strlen(buf);
			for(int i=0;i<l;i++)d[i]=buf[l-1-i]-'0';
		}

		bool operator<(const Int &q) const
		{
			if(l!=q.l)return l<q.l;
			for(int i=l-1;i>=0;i--)if(d[i]!=q.d[i])return d[i]<q.d[i];
			return false;
		}

		void sqr(const Int &x)
		{
			l=0;
			for(int i=0;i<x.l;i++)
				for(int j=0;j<x.l;j++)
				{
					int k=i+j;
					while(l<=k)d[l++]=0;
					d[k]+=x.d[i]*x.d[j];
					while(d[k]>=10)
					{
						if(k+1==l)d[l++]=0;
						d[k+1]+=d[k]/10;
						d[k++]%=10;
					}
				}
		}

		void println() const
		{
			if(l==0){puts("0");return;}
			for(int i=l-1;i>=0;i--)putchar('0'+d[i]);
			putchar('\n');
		}
};

const int LMAX=50;

int L; char D[LMAX];
vector<Int> V;

void output()
{
	static Int x;
	D[L]='\0';
	x=D;
	V.resize(V.size()+1);
	V.back().sqr(x);
}

void build(int dep,int rem)
{
	static const int sqr[]={0,1,4};
	if(rem==0||L-1-dep<dep){output();return;}
	for(int i=(dep!=0?0:1);i<=2;i++)
	{
		int j=sqr[i];
		if(L-1-dep!=dep)j<<=1;
		if(rem<j)continue;
		D[dep]='0'+i;
		D[L-1-dep]='0'+i;
		build(dep+1,rem-j);
	}
}

void build()
{
	L=1;
	D[0]='0';output();
	D[0]='1';output();
	D[0]='2';output();
	D[0]='3';output();
	for(L=2;L<=50;L++)build(0,9);
}

int main()
{
	build();
	int t;
	scanf("%d",&t);
	for(int s=1;s<=t;s++)
	{
		static char buf[102];
		static Int a,b;
		scanf("%s",buf);a=buf;
		scanf("%s",buf);b=buf;
		printf("Case #%d: %d\n",s,(int)((upper_bound(V.begin(),V.end(),b)-V.begin())-(lower_bound(V.begin(),V.end(),a)-V.begin())));
	}
	return 0;
}
