#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
	int t,n,j,alow1,ahigh1,blow1,bhigh1,ctr1,ctr2,i,ahigh2,blow2,bhigh2;
	float a[1001],b[1001];
	FILE *ifp, *ofp;
	char outputFilename[] = "DeceitfulWarOutput.txt";
	
	ifp = fopen("D-large.in", "r");
	ofp = fopen(outputFilename, "w");
	fscanf(ifp,"%d", &t);
	
	for(i=1;i<=t;i++)
	{
		fscanf(ifp,"%d",&n);
		for(j=0;j<n;j++)
			fscanf(ifp,"%f",&a[j]);
		for(j=0;j<n;j++)
		    fscanf(ifp,"%f",&b[j]);
		    
		sort(a,a+n);
		sort(b,b+n);
		
		alow1=0;blow1=0;ctr1=0;
		ahigh1=n-1;bhigh1=n-1;
		
		ctr2=0;ahigh2=n-1;blow2=0,bhigh2=n-1;
		
		while(alow1!=ahigh1+1 && blow1!=bhigh1+1)
		{
			if(a[alow1]<b[blow1])
			{
				alow1++;
				bhigh1--;
			}
			else
			{
				alow1++;
				blow1++;
				ctr1++;
			}
		}
		while(ahigh2>=0 && blow2!=bhigh2+1)
		{
			if(a[ahigh2]>b[bhigh2])
			{
				ahigh2--;
				blow2++;
				ctr2++;
			}
			else
			{
				ahigh2--;
				bhigh2--;
			}
		}
		fprintf(ofp,"Case #%d: %d %d",i, ctr1,ctr2);
		
		if(i!=t)
		   fprintf(ofp,"\n");
	}
}
