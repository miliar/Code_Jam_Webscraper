#include <cstdio>
#include <cstring>

using namespace std;

char s[101];

long cNbr (long a, long b){
	
	long i,c=0,cmax=0;
	c=cmax=0;
	for(i=a;i<=b;i++){
		if(s[i]!='a' && s[i]!='e' && s[i]!='i' && s[i]!='o' && s[i]!='u')
			c++;
		else
		{
			if(cmax<c)
				cmax=c;
			c=0;
		}
	}
	if(c>cmax)
		cmax=c;
	return cmax;
}

long tC,n,i,j,c2;

int main () {
	
	freopen ("in","r",stdin);
	freopen ("out","w",stdout);
	
	scanf("%ld\n",&tC);
	long ct=0;
	while (tC--)
	{
		ct++;
		c2=0;
		scanf("%s",s);
		scanf("%ld\n",&n);
		long str=strlen(s);
		for(i=0;i<str;i++)
			for(j=i;j<str;j++)
				if(cNbr(i,j)>=n)
					c2++;
		
		printf("Case #%ld: %ld\n",ct,c2);
	}
	return 0;
}
