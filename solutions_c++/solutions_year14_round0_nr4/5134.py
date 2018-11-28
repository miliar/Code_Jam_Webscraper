#include<stdio.h>
//#include<conio.h>
int main()
{       //clrscr();
	int t,n,by[50],g[50],b2[50],g2[50],s,i,k,l,m,j,x,y,z,flag;
	float a[10], b[10];
	scanf("%d",&t);
	for(i=0; i<t; i++)
	{       by[i]=0;
		g[i]=0;
		b2[i]=0;
		g2[i]=0;
		scanf("%d",&n);
		j=n;
		   for(k=0; k<n; k++)
		   {
			scanf("%f",&a[k]);
		   }
		   for(k=0; k<j; k++)
		   {
			scanf("%f",&b[k]);
		   }
		   for(l=0; l<n-1; l++)
		   {
			for(m=0; m<n-l-1; m++)
			{
				if(a[m]>a[m+1])
				{
					a[m]=a[m]+a[m+1];
					a[m+1]=a[m]-a[m+1];
					a[m]=a[m]-a[m+1];
				}
			}
		   }
		    for(l=0; l<j-1; l++)
		   {
			for(m=0; m<j-l-1; m++)
			{
				if(b[m]>b[m+1])
				{
					b[m]=b[m]+b[m+1];
					b[m+1]=b[m]-b[m+1];
					b[m]=b[m]-b[m+1];
				}
			}
		   }
		   x=0;
		   y=0;
		       while(x<n)
		       {	if(a[x]<b[y])
			{
			   x++;

			 by[i]++;
			}
			 else if(a[x]>b[y])
			{  x++;
			y++;
			 g[i]++;
			}
			};
			   x=0; y=0;
			while(x<n)
			{
				if(a[x]<b[y])
				{
					x++; y++; b2[i]++;
				}
				else if(a[x]>b[y])
				{

					for(z=0; z<n; z++)
					{	if(a[x]<b[z])
						{ flag=z; b2[i]++;
						break;}
						else
						flag=0;
					}
					if(flag==0)
					g2[i]++;
					for(s=flag; s>y; s--)
					b[s]=b[s-1];
					y++;

				       x++;
				}
			};

		   }
		   for(i=0; i<t; i++)
		    printf("\nCase #%d: %d %d",i+1,g[i],g2[i]);
	return 0;
	}






