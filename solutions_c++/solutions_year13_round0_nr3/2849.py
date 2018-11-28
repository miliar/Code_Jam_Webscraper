#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<cmath>

using namespace std;

int B[11],tot,T,ans,a,b,i;

inline bool P(int a,int b) { return (b*b==a)?true:false; }

inline bool Xun(int t)
{	int i,l=0;
	while (t>0) B[++l]=t%10,t/=10;
	for (i=1;i<=(l/2);i++) if (B[i]!=B[l-i+1]) return false; return true; 
}

int main()
{
//	freopen("C.in","r",stdin);
//	freopen("C_test.out","w",stdout);
	scanf("%d",&T);
	for (tot=1;tot<=T;tot++)
	{	printf("Case #%d: ",tot);
		scanf("%d%d",&a,&b); ans=0;
		for (i=a;i<=b;i++)
			if (P(i,sqrt(i))&&Xun(i)&&Xun(sqrt(i))) ans++;
		printf("%d\n",ans);
		}
	return 0;
}
