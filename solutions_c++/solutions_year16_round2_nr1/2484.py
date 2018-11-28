#include <cstring>
#include <cstdio>

char s[2010];
int cnt[10],c[26];

int main ()
{
	FILE *in=fopen("A-small-attempt0.in","r");
	FILE *out=fopen("output.txt","w");
	int T,n,t;

	fscanf (in,"%d",&T);
	for (int t=1;t<=T;t++)
	{
		fprintf (out,"Case #%d: ",t);
		fscanf (in,"%s",s);
		n=strlen(s);
		int i,r,j;
		for (i=0;i<10;i++)
			cnt[i]=0;
		for (i=0;i<26;i++)
			c[i]=0;
		for (i=0;i<n;i++)
			c[s[i]-65]++;

		cnt[0]=r=c['Z'-65];
		if (1)// 0 zero
		{
			c['Z'-65]-=r;
			c['E'-65]-=r;
			c['R'-65]-=r;
			c['O'-65]-=r;
		}
		cnt[6]=r=c['X'-65];
		if (1)// 6
		{
			c['S'-65]-=r;
			c['I'-65]-=r;
			c['X'-65]-=r;
		}
		cnt[7]=r=c['S'-65];
		if (1)// 7
		{
			c['S'-65]-=r;
			c['E'-65]-=r;
			c['V'-65]-=r;
			c['E'-65]-=r;
			c['N'-65]-=r;
		}
		cnt[8]=r=c['G'-65];
		if (1)// 8
		{
			c['E'-65]-=r;
			c['I'-65]-=r;
			c['G'-65]-=r;
			c['H'-65]-=r;
			c['T'-65]-=r;
		}
		cnt[2]=r=c['W'-65];
		if (1)// 2
		{
			c['T'-65]-=r;
			c['W'-65]-=r;
			c['O'-65]-=r;
		}
		cnt[5]=r=c['V'-65];printf ("%d",cnt[5]);
		if (1)// 5
		{
			c['F'-65]-=r;
			c['I'-65]-=r;
			c['V'-65]-=r;
			c['E'-65]-=r;
		}
		
		cnt[4]=r=c['F'-65];
		if (1)// 4
		{
			c['F'-65]-=r;
			c['O'-65]-=r;
			c['U'-65]-=r;
			c['R'-65]-=r;
		}

		cnt[1]=r=c['O'-65];
		if (1)// 1
		{
			c['O'-65]-=r;
			c['N'-65]-=r;
			c['E'-65]-=r;
		}
		
		cnt[9]=r=c['I'-65];
		if (1)// 9
		{
			c['N'-65]-=r;
			c['I'-65]-=r;
			c['N'-65]-=r;
			c['E'-65]-=r;
		}
		cnt[3]=r=c['H'-65];
		if (1)// 3
		{
			c['T'-65]-=r;
			c['H'-65]-=r;
			c['R'-65]-=r;
			c['E'-65]-=r;
			c['E'-65]-=r;
		}
		for (i=0;i<10;i++)
			for(j=0;j<cnt[i];j++)
				fprintf(out, "%d",i);
		fprintf(out, "\n");
	}
}
