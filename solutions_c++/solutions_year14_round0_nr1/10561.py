#include<iostream>
#include<stdlib.h>
#include<time.h>
using namespace std;
main()
{

	int T;
	cin>>T;
	int g1,g2,x;
	int A[16];	
	for(int t=1;t<=T;t++)
	{

		cin>>g1;
		int c=1;
		for(int i=0;i<16;i++)
		{
			A[i]=0;
		}
		
		for(int i=0;i<16;i++)
		{

			cin>>x;
			if(c==g1)
			{
				A[x]=1;			
			}
			if((i+1)%4==0)	
			{
				c++;
			}


		}

		cin>>g1;
		c=1;
		int count=0;
		int num=0;
		for(int i=0;i<16;i++)
		{

			cin>>x;
			if(c==g1)
			{
				if(A[x]==1)
				{
					count++;
					num=x;
				}
							
			}
			if((i+1)%4==0)	
			{
				c++;
			}

		}

		if(count==1)
		{
			cout<<"Case #"<<t<<": "<<num<<endl;
		}
		else if(count==0)
		{
			cout<<"Case #"<<t<<": Volunteer cheated!"<<endl;
		}
		else
		{

			cout<<"Case #"<<t<<": Bad magician!"<<endl;
		}

	}
}

