#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
using namespace std;
int main()
{
	int a[16],b[16],i,j,x,n,m,t,k,count,temp;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		count=0;
	cin>>n;
	for(j=0;j<16;j++)
	{
	cin>>a[j];
	}	
	cin>>m;
	for(j=0;j<16;j++)
	{
	cin>>b[j];
	}
	for(k=(4*n-4);k<(4*n);k++)
	{
		for(j=(4*m-4);j<(4*m);j++)
		{
			if(a[k]==b[j])
			{
				count++;
				temp=a[k];
				}
			}
			}
			if(count==1)
			{
			printf("Case #%d: %d \n",i,temp);
				}
				else if(count>1)
				{ 
					printf("Case #%d: Bad magician!\n",i);
					}
					else if(count==0)
					{
					printf("Case #%d: Volunteer cheated!",i);
						}
		
		}
	return 0;
}
