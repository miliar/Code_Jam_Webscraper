#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	
	int cases,no,test,i,j,count_d,count_w,ans2;
	
	scanf("%d",&cases);
	test = cases;
	while(cases)
	{
		scanf("%d",&no);
		
		double a[no+3],b[no+3],t;
		
		for(i=0;i<no;i++)
			scanf("%lf",&a[i]);
		for(i=0;i<no;i++)
			scanf("%lf",&b[i]);
		
	
		
		for(i=0;i<no-1;i++)
		{
			for(j=0;j<no-1;j++)
			{
				if(a[j]>a[j+1])
				{
					t=a[j];
					a[j]=a[j+1];
					a[j+1]=t;
				}
			}
		}
		
		for(i=0;i<no-1;i++)
		{
			for(j=0;j<no-1;j++)
			{
				if(b[j]>b[j+1])
				{
					t=b[j];
					b[j]=b[j+1];
					b[j+1]=t;
				}
			}
		}
		
	
		
		i=j=no-1;
		count_d = 0;
		for(;;)
		{
			if(a[i]>b[j])
			{
				count_d++;
				i--;
				j--;
				if(j==-1)
					break;		
			}
			else
			{
				j--;
				if(j==-1)
					break;
			}
			
		}
		
		i=j=0;
		count_w=0;
		for(;;)
		{
			if(b[j]>a[i])
			{
				count_w++;
				i++;
				j++;
				if(j>=no)
					break;	
			}	
			else
			{
				j++;
				if(j>=no)
					break;
			}
			
			
		
		}
		ans2 = no - count_w;
		//cout<<"Case #"<<test-cases+1<<": "<<count_d<<" "<<ans2<<endl;
		
		printf("Case #%d: %d %d\n",test-cases+1,count_d,ans2);
		cases--;	
	}



cin.get();
cin.get();
return 0;
}
