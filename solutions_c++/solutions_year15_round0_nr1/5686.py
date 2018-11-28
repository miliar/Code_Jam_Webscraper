#include <cstdio>
using namespace std;
int main()
{
	int t,s[1111],i,n,cum[1111],max,T;
	FILE * fr=fopen("A-large.in","r");
	FILE * fw=fopen("A.out","w");
	fscanf(fr,"%d",&t);
	T=t;
	while(t--)
	{
		fscanf(fr,"%d",&n);
		fgetc(fr);
		cum[0]=max=0;
		for(i=1;i<=n+1;i++)
		{
			s[i]=fgetc(fr)-'0';
			cum[i]=s[i]+cum[i-1];
			if(s[i]>0&&(i-1)-cum[i-1]>max)
				max=(i-1)-cum[i-1];
		}
		fprintf(fw, "Case #%d: %d\n",(T-t),max);
	}
	fclose(fr);
	fclose(fw);
}