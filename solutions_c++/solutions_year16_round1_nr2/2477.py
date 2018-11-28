#include <cstring>
#include <cstdio>
#include <algorithm>

#define INF -1

int T,t,n,i,j,k,l,r,c;
int a[60][60],ans,b[60][60];

struct data{
	int a[60];
};

data s[101],ch[102];

bool com (data x, data y)
{
	int i;

	for (i=1;i<n;i++)
	{
		if (x.a[i]<y.a[i])
			return true;
		else if (x.a[i]>y.a[i])
			return false;
	}
	return true;
}

int fit (int x, int m, int rc)
{
	int i;
	if (rc==0)	// За
	{
		for (i=1;i<=n;i++)
			if (a[x-1][i]!=INF && s[m].a[i] <= a[x-1][i] || a[x][i]!=INF&&s[m].a[i]!=a[x][i])
				return 0;
		return 1;
	}
	else
	{
		for (i=1;i<=n;i++)
			if (a[i][x-1]!=INF && s[m].a[i] <= a[i][x-1] || a[i][x]!=INF&&s[m].a[i]!=a[i][x])
				return 0;
		return 1;
	}
}

void go (int x, int y, int h)
{
	int i,j,r[51],m;
	if (x>=n&&y>=n&&x+y>2*n+h)
	{
		printf ("%d %d--\n",x,y);
		for (i=1;i<=n;i++,printf ("\n"))
			for (j=1;j<=n;j++)
				b[i][j]=a[i][j],printf ("%d ",a[i][j]);
		for (i=1;i<=n;i++)
			for (j=1;j<=n;j++)
				if (a[i][j]==INF)
					ans++;
		if (!ans){
			ans=1;
			for (i=1;i<=n;i++)
				for (j=1;j<=n;j++)
				{
					ch[i].a[j]=a[i][j];
					ch[i+n].a[j]=a[j][i];
				}
		}
		else ans=0;
		return;
	}
	if (ans) return;
	m=x+y-1-h;
	/*printf ("%d %d--- ",x,y); for (i=1;i<=n;i++)printf("%d",s[m].a[i]);printf ("\n");
	for (i=1;i<=n;i++,printf ("\n"))
		for (j=1;j<=n;j++)
			printf ("%d ",a[i][j]);getchar();*/
	if (!ans&&x<=n&&fit (x,m,0))
	{
		for (i=1;i<=n;i++) r[i]=a[x][i],a[x][i]=s[m].a[i];
		go (x+1,y,h);
		for (i=1;i<=n;i++) a[x][i]=r[i];
	}
	if (!ans&&x<n&&!h && fit (x+1,m,0))
	{
		for (i=1;i<=n;i++) r[i]=a[x+1][i],a[x+1][i]=s[m].a[i];
		go (x+2,y,1);
		for (i=1;i<=n;i++) a[x+1][i]=r[i];
	}

	if (!ans&&y<=n&&fit (y,m,1))
	{
		for (i=1;i<=n;i++) r[i]=a[i][y],a[i][y]=s[m].a[i];
		go (x,y+1,h);
		for (i=1;i<=n;i++) a[i][y]=r[i];
	}
	if (!ans&&y<n&&!h && fit (y+1,m,1))
	{
		for (i=1;i<=n;i++) r[i]=a[i][y+1],a[i][y+1]=s[m].a[i];
		go (x,y+2,1);
		for (i=1;i<=n;i++) a[i][y+1]=r[i];
	}
}

int main ()
{
	FILE *in=fopen ("input.txt","r");
	FILE *out=fopen ("output.txt","w");

	fscanf (in,"%d",&T);
	for (t=1;t<=T;t++)
	{
		fscanf (in, "%d",&n);
		for (i=1;i<n*2;i++)
			for (j=1;j<=n;j++)
				fscanf (in,"%d",&s[i].a[j]);
		fprintf (out, "Case #%d: ",t);
		std::sort (s+1,s+n*2,com);

		for (i=1;i<=n;i++)
			for (j=1;j<=n;j++)
				a[i][j]=INF;
		ans=0;
		go (1,1,0);
		/*for (k=1;k<=n*2;k++)
		{
			for (i=1;i<=n;i++)
				for (j=1;j<=n;j++)
					a[i][j]=INF;
			r=c=1;
			for (i=1;i<n*2;i++)
			{
				if (k==r && k<=n) r++;
				else if (k==c && k>n) c++;
				if (c>r&& fit(c,i,1))
				{
					for (j=1;j<=n;j++)
						a[j][c]=s[i].a[j];
					c++;
				}
				else if (fit(r,i,0))
				{
					for (j=1;j<=n;j++)
						a[r][j]=s[i].a[j];
					r++;
				}
				else if (fit(c,i,1))
				{
					for (j=1;j<=n;j++)
						a[j][c]=s[i].a[j];
					c++;
				}
			}
			c=0;
			for (i=1;i<=n;i++)
				for (j=1;j<=n;j++)
					if (a[i][j]==INF)
						c=1;
			if (c==0)
				break;
		}*/
		for (i=1;i<=n;i++,printf ("\n"))
			for (j=1;j<=n;j++)
				printf ("%d ",b[i][j]);
		printf ("\n");

		if (!ans)
		for (i=1;i<=n;i++)
			for (j=1;j<=n;j++)
			{
		//		ch[i].a[j]=a[i][j];
			//	ch[i+n].a[j]=a[j][i];
			}
		
		for (i=1;i<=n*2;i++)
		{
			//for(k=1;k<=n;k++) printf ("%d ",ch[i].a[k]); printf ("\n");
			r=0;
			for (j=1;j<n*2;j++)
			{
				for (k=1;k<=n;k++)
					if (ch[i].a[k]!=s[j].a[k])
						break;
				if (k>n)
				{
					r=1;
					for (k=1;k<=n;k++)
						s[j].a[k]=0;
					break;
				}
			}
			if (r==0)
				for (j=1;j<=n;j++)
					fprintf (out, "%d ",ch[i].a[j]);
		}

		fprintf (out,"\n");
	}
}