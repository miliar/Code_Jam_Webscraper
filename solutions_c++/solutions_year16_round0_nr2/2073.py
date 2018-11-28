#include<cstdio>
#include<cstring>
#define fo(i,a,b) for(int i=a;i<=b;i++)
using namespace std;

const int maxn=105;

int n;
char s[maxn];

int T;
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	scanf("%d\n",&T);
	fo(Ti,1,T)
	{
		printf("Case #%d: ",Ti);
		
		scanf("%s\n",s+1);
		n=strlen(s+1);
		
		int size=1;
		fo(i,2,n) size+=(s[i]!=s[i-1]);
		
		if (s[n]=='+') printf("%d\n",size-1); else printf("%d\n",size);
	}
}