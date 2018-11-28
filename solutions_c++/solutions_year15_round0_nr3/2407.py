#include<iostream>
#include<fstream>
#include<cstdio>
#define maxn 1000000
using namespace std;
ifstream fin("b.in");
ofstream fout("b.out");
long long aa[10][10]={{0},
	{0,1,2,3,4},
	{0,2,-1,4,-3},
	{0,3,-4,-1,2},
	{0,4,3,-2,-1}
};
long long abs(long long x)
{
	if(x<0)return -x;else return x;
}
long long sig(long long x)
{
	if(x<0)return -1;else return 1;
}
long long mul(long long a,long long b)
{
	long long u=abs(a),v = abs(b);
	long long ret=aa[u][v];
	return sig(a)*sig(b)*ret;
}
long long trans(char c)
{
	if(c=='1')return 1;
	if(c=='i')return 2;
	if(c=='j')return 3;
	if(c=='k')return 4;
}
long long sum[maxn];
char ch[maxn];
int main()
{
	long long t,n,m,cas=0;
        fin>>t;
	while(t--)
	{
		fin>>n>>m>>(ch+1);
		if(m>16)m = m % 4 + 12;
		for(int i=1;i<m;i++)
		{
			for(int j=1;j<=n;j++)
			{
				ch[i*n+j]=ch[j];
			}
		}
		long long len = n*m ;
		sum[1] = trans(ch[1]);
		for(int i=2;i<=n*m;i++)
		{
			sum[i]=mul(sum[i-1],trans(ch[i]));
		}
		if(sum[len]!=-1)
		{
			fout<<"Case #"<<++cas<<": NO"<<endl;
			continue;
		}
		long long ii=len+1,kk=-1;
		for(int i=1;i<=len;i++)
		{
			if(sum[i]==2)
			{
				ii=i;
				break;
			}
		}
		long long su=1;
		for(int i=len;i>=1;i--)
		{
			su=mul(trans(ch[i]),su);
			if(su==4)
			{
				kk=i;
				break;
			}
		}
		if(ii<kk)
		{
			fout<<"Case #"<<++cas<<": YES"<<endl;
		}
		else fout<<"Case #"<<++cas<<": NO"<<endl;
	}
	return 0;
}
