#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
int t;
scanf("%d",&t);
int itr=0;
while(itr<t)
	{itr++;
	
	 int n;
	 scanf("%d",&n);
	 float a[n],b[n];
	 for(int i=0;i<n;i++)
	 	scanf("%f",&a[i]);
	for(int i=0;i<n;i++)
	 	scanf("%f",&b[i]);
	 
	 sort(a,a+n);
	 sort(b,b+n);
	 /*
	 for(int i=0;i<n;i++)
	 	printf("%0.3f ",a[i]);
	 	printf("\n");
	for(int i=0;i<n;i++)
	 	printf("%0.3f ",b[i]);
	 	printf("\n");*/
	 int bac=n-1;
	 int froc=0;
	 int i;
	 int answer=0;
	 for(i=0;i<n;i++)
	 	{
	 	 if(a[i]<b[froc])
	 	 	{
	 	 	 bac--;
	 	 	}
	 	else
	 		{
	 		 answer++;
	 		 froc++;
	 		}
	 	}
	 	printf("Case #%d: %d ",itr,answer);
	 	 froc=0;
	 	answer=0;
	 	for(int i=0;i<n;i++)
	 	{if(froc>=n)
	 		break;
	 		 //cout<<i<<" "<<froc<<" "<<answer<<"it\n";
	 	 if(a[i]<b[froc])
	 	 {froc++;
	 	 //cout<<i<<" "<<froc<<" "<<answer<<"\n";
	 	 }
	 	 else
	 	 	{
	 	 	 while(froc<n && a[i]>b[froc])
	 	 		{
	 	 		answer++;
	 	 		froc++;
	 	 	
	 	 		//cout<<i<<" "<<froc<<" "<<answer<<"hell\n";
	 	 		}
			i--;
			}
	 	
		 }
	
	printf("%d\n",answer);
	}
}
