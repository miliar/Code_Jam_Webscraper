#include <iostream>
#include <stdio.h>
using namespace std;
 
int main() 
{
int t,p,a,arr_p[4][4],arr_a[4][4],r_p[4],r_a[4];
int i,j,c=1,com=0,comc;	
	cin>>t;
	while(t--)
	{
		cin>>p;
		for(i=0;i<4;i++)
			{
				for(j=0;j<4;j++)
				cin>>arr_p[i][j];
			}
			r_p[0]=arr_p[p-1][0];r_p[1]=arr_p[p-1][1];r_p[2]=arr_p[p-1][2];r_p[3]=arr_p[p-1][3];
		cin>>a;
		for(i=0;i<4;i++)
			{
				for(j=0;j<4;j++)
				cin>>arr_a[i][j];
			}
			r_a[0]=arr_a[a-1][0];r_a[1]=arr_a[a-1][1];r_a[2]=arr_a[a-1][2];r_a[3]=arr_a[a-1][3];
			
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(r_p[i]==r_a[j])
					{com++;
					comc=r_p[i];	
					}
			}
		}
	if(com==1)
	printf("Case #%d: %d\n",c,comc);
	else if(com>1)
	printf("Case #%d: Bad magician!\n",c);
	else if(com==0)
	printf("Case #%d: Volunteer cheated!\n",c);
	com=0;c++;
	}
	
	return 0;
}