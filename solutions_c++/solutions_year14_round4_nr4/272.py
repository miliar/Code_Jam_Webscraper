#include <stdio.h>
#include <string.h>

char s[2010][20];
char s2[2010][20];
char temps[2010][20];
int m ,n;
int r[2010];
int lala[200];
void f(int p);
void mergesort(int n1 ,int n2);
int temp1;
int ans1 ,ans2;
int main(void)
{
	int t ,i;
	int j;
	
	scanf("%d" ,&t);
	for (i=1 ; i<=t ; i++)
	{
		scanf("%d %d" ,&m ,&n);
		temp1=n;		
		for (j=1 ; j<=m ; j++)
		{
			scanf("%s" ,s[j]);
			temp1+=strlen(s[j]);
		}
		for (j=1 ; j<=n ; j++)
		{
			lala[j]=0;
		}
		ans1=100000000;
		f(1);
		printf("Case #%d: %d %d\n" ,i ,temp1-ans1 ,ans2);
	}

	return 0;
}

void f(int p)
{
	int i ,j ,j2 ,j3;
	int z;
	int np;
	int temp2;
	
	for (i=1 ; i<=n ; i++)
	{
		r[p]=i;
		lala[i]++;
		if (p==m)
		{
			z=1;
			for (j=1 ; j<=n ; j++)
			{
				if (lala[j]==0)	
				{
					z=0;	
					break;
				}
			}
			if (z)
			{
				temp2=0;
				for (j=1 ; j<=n ; j++)
				{
					np=0;
					for (j2=1 ; j2<=m ; j2++)
					{
						if (r[j2]==j)
						{
							np++;
							strcpy(s2[np],s[j2]);	
						}	
					}
					mergesort(1,np);
					for (j2=1 ; j2<np ; j2++)
					{
						for (j3=0 ; ; j3++)
						{
							if (s2[j2][j3]==0||s2[j2+1][j3]==0)	
							{
								break;	
							}
							else if (s2[j2][j3]==s2[j2+1][j3])
							{
								temp2++;
							}
							else
							{
								break;	
							}
						}
					}					
				}
				if (temp2<ans1)
				{
					ans1=temp2;	
					ans2=1;
				}
				else if (temp2==ans1)
				{
					ans2++;	
				}
			}
		}
		else
		{
			f(p+1);
		}
		lala[i]--;
	}
}

void mergesort(int n1 ,int n2)
{
	int a1 ,a2 ,n12;
	int i ,j;
	int z;
	double k1 ,k2;
	
	if (n1<n2)
	{	
		n12=(n1+n2)/2;
		mergesort(n1,n12);
		mergesort(n12+1,n2);
		for (i=n1 ; i<=n2 ; i++)
		{
			strcpy(temps[i],s2[i]);
		}
		a1=n1;
		a2=n12+1;
		for (i=n1 ; (a1<=n12 && a2<=n2) ;i++)
		{
			if (strcmp(temps[a1],temps[a2])<=0)
			{
				strcpy(s2[i],temps[a1]);
				a1++;
			}
			else
			{
				strcpy(s2[i],temps[a2]);
				a2++;				
			}
		}
		if (a1>n12)
		{
			for (j=a2 ; j<=n2 ; j++ , i++)
			{
				strcpy(s2[i],temps[j]);
			}
		}
		else
		{
			for (j=a1 ; j<=n12 ; j++ , i++)
			{
				strcpy(s2[i],temps[j]);
			}			
		}
	}
}
