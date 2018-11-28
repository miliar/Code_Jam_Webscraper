#include <iostream>
using namespace std;

int main() {
		int t;
		cin>>t;
		for(int k=1;k<=t;k++)
		{
			int num_1,num_2,count=0,pos=0,a1[4][4],a2[4][4];
			cin>>num_1;
			for(int i=0;i<4;i++)
			{
				for(int j=0;j<4;j++)
				{
					cin>>a1[i][j];
				}
			}	
			cin>>num_2;
			for(int i=0;i<4;i++)
			{
				for(int j=0;j<4;j++)
				{
					cin>>a2[i][j];
				}
			}
	
				for(int i=0;i<4;i++)
				{
					for(int j=0;j<4;j++)
					{	
						if(a1[num_1-1][i]==a2[num_2-1][j] )
						{
							++count;
							if(count==1)
							{
								pos=i;
							}
						}
						
					}	
				}
			
			  
			if(count==1)
			{
				cout<<"Case #"<<k<<": "<<a1[num_1-1][pos]<<"\n";
			}
			else if( count>1) 
			{
			
				cout<<"Case #"<<k<<": Bad magician!\n";			
			}
			
			else if(count==0)
			{
				cout<<"Case #"<<k<<": Volunteer cheated!\n";
			}
			
		
	}
	return 0;
}