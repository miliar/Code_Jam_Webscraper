#include<stdio.h>
void quicksort(double a[], int n);
main()
{
	FILE *ifp;
	FILE *ofp;
	int t,a,j,i,l,point;
	int dpoint,y,x;
	ifp=fopen("test3.in","r");
	ofp=fopen("output3.txt","w");
	fscanf(ifp,"%d",&t);
	for(i=0;i<t;i++)
	{point=0;dpoint=0;x=0;y=0;
	fscanf(ifp,"%d",&a);
	double n[a];
	double k[a];
	double s[a];
	double p[a];
	
	for(j=0;j<a;j++)	
		fscanf(ifp,"%lf",&n[j]);
		for(j=0;j<a;j++)			
		fscanf(ifp,"%lf",&k[j]);		
	quicksort(n,a);
	quicksort(k,a);
	for(j=0;j<a;j++)
	{
	p[j]=k[j];
	s[j]=n[j];
	}
	for(j=0;j<a;j++)
	{
		if(p[x]>s[j])
		{
		
			p[a-y]=0;
			y++;
		}
		else{
			p[x]=0;
			x++;
			dpoint++;
		}
		if(x==a)
		break;
	}

	for(j=0;j<a;j++)
	{
		int count=0;
		for(l=0;l<a;l++)
		{
			if(k[l]>n[j])
			{
				k[l]=0;
				break;
			}
			else
			count++;
			
			if(count==a)
			{
				point++;
				
			}
		}
	}
	fprintf(ofp,"Case #%d: %d %d\n",i+1,dpoint,point);

	}
		fclose(ifp);
	fclose(ofp);
}
void quicksort(double a[], int n)
	 {
    if (n <= 1) return;
    double p = a[n/2];
    double b[n], c[n];
    int i, j = 0, k = 0;
    for (i=0; i < n; i++) {
        if (i == n/2) continue;
        if ( a[i] <= p) b[j++] = a[i];
        else            c[k++] = a[i];
    }
    quicksort(b,j);
    quicksort(c,k);
    for (i=0; i<j; i++) a[i] =b[i];
    a[j] = p;
    for (i= 0; i<k; i++) a[j+1+i] =c[i]; 
	}
