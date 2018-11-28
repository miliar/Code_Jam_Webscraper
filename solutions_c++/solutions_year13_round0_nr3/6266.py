#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<string>
#include<algorithm>

using namespace std;
int T;
long long A,B;

char* change(long long x)
{		
	char *s=new char[110];
	int cnt=0;
	while(x)
		{
		int a=x%10;
		x/=10;
		s[cnt++]=48+a;
		}
	s[cnt]='\0';
return s;
}

bool hui(char* ww)
{
	int len=strlen(ww);
	for(int i=0;i<=len/2;i++)
		{
		if(ww[i]!=ww[len-1-i])
			return false;
		}
return true;
}
int main()
{		
	//freopen("C:\\Users\\think\\Desktop\\C-small-attempt0.in","r",stdin);
	//freopen("C:\\Users\\think\\Desktop\\c.out","w",stdout);
	scanf("%d",&T);
	for(int y=1;y<=T;y++)
		{
		scanf("%lld%lld",&A,&B);
		double a=sqrt(A*1.0);
		double b=sqrt(B*1.0);
		long long aa,bb;
		if(abs(a-long long(a))>0.000001)
			aa=long long(a)+1;
		else
			aa=long long (a);
		bb=long long (b);
		long long m;
		int ans=0;
		for(m=aa;m<=bb;m++)
			{
			long long tt=m*m;
			char* kk=change(tt);
			char* sss=change(m);
			if(hui(kk)&&hui(sss))
				ans++;
			}
		printf("Case #%d: %d\n",y,ans);
	}
	return 0;
}

