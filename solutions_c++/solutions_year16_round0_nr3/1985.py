#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
char s[50];
const int maxn=1e7+100;
LL p[maxn],pnum,ans[20],anum;
bool isnp[maxn];
void get_prime()
{
	pnum=0;
	int i,j;
	for(i=2;i<maxn;++i)
	{
		if(!isnp[i])p[pnum++]=i;
		for(j=0;j<pnum&&p[j]*i<maxn;++j)
		{
			isnp[p[j]*i]=true;
			if(i%p[j]==0)break;
		}
	}
}
bool isprime(LL v)
{
	for(int i=0;i<pnum&&p[i]*p[i]<=v;++i)
		if(v%p[i]==0)
		{
			ans[anum++]=p[i];
			return false;
		}
	return true;
}
char num[50];
bool check(int beg)
{
	int len,i=0;
	if(!isnp[beg])return false;
	LL v,bb;
	anum=0;
	num[16]='\0';
	for(int i=15;i>=0;--i,beg>>=1)
		if(beg&1)num[i]='1';
		else num[i]='0';
	if(num[15]!='1')return false;
	for(int base=2;base<=10;++base)	
	{
		v=0;
		for(bb=1,i=15;i>=0;--i,bb*=base)
			if(num[i]=='1')v=v+bb;
		//cout <<v<<" "<<num<<" "<<isprime(v)<<endl;system("pause");
		if(isprime(v))return false;
	}
	return true;
}
int main()
{
	get_prime();
	int beg=(1<<15)+1,J=50;
	FILE *fp=fopen("C.out","w");
	for(beg;beg<(1<<16)&&J;++beg)
	{
		if(check(beg))
		{
			fprintf(fp,"%s",num);
			for(int i=0;i<anum;++i)fprintf(fp," %d",ans[i]);fprintf(fp,"\n");
			--J;
			cerr<<"ac:"<<beg<<endl;
		}
		//cerr<<beg<<endl;
	}
}
