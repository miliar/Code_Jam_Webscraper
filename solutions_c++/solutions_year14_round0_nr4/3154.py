#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <vector>

using namespace std;

int main ()
{
	FILE *f1,*f2;
	f1=fopen("D-large.in","r");
	f2=fopen("out1.txt","w");
	int t;
	fscanf(f1,"%d",&t);
	int k,i,j,startb,endb,deceit,war,n;
	for(k=0;k<t;k++)
	{
		fscanf(f1,"%d",&n);
		vector<float> a(n+1);
		vector<float> b(n+1);
		for(i=0;i<n;i++)
		{
			fscanf(f1,"%f ",&a[i]);	
		}
		for(i=0;i<n;i++)
		{
			fscanf(f1,"%f ",&b[i]);	
		}

		sort(a.begin(),a.end());
		sort(b.begin(),b.end());
		

		startb=1;
		endb=n;
		deceit=0;
		for(i=1;i<n+1;i++)
		{
			
			if(a[i]<b[startb])
				{
					endb--;
				}
				else
				{
					deceit++;
					startb++;
				}
		}
		j=1;
		war=0;
		for(i=1;(i<n+1)&&(j<n+1);)
		{
			//printf("%f %f\n",a[i],b[j]);
			if(a[i]<b[j])
			{
				//printf(" dd \n");
				i++;
				j++;
			}
			else{
				j++;
				war++;
			}

		}
		//war=war+(n-i+1);

		fprintf(f2,"Case #%d: %d %d\n",k+1,deceit,war);		
	}
	fclose(f1);
	fclose(f2);
}