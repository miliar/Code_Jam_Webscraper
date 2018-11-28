#include <iostream>

using namespace std;


int main() 
{
	
int T,X,Y;
	
int i,j,k,num,cnt=0;
	
int x1[4][4],x2[4][4];
	
cin>> T;
	
for(i=0;i<T;i++)
	
{  
cnt=0;
	   
num=0;
		
cin>>X;
		
		
for(j=0;j<4;j++)
		
{
   
for(k=0;k<4;k++)
			
{
				
cin>>x1[j][k];
			
}
		
}
		
cin>>Y;
		
for(j=0;j<4;j++)
		
{   
			
for(k=0;k<4;k++)
			
{
				
cin>>x2[j][k];
			
}
		
}
		
		
for(j=0;j<4;j++)
		
{   
			
for(k=0;k<4;k++)
			
{
				
if(x1[X-1][j]==x2[Y-1][k])
				
{
					
cnt++;
				
num=x1[X-1][j];
				
}
			
}
		
}
		

	if(cnt==1)
	
{
		
cout<<"case #"<<i<<": "<<num<<"\n";

	
	}
	
else if(cnt>1)

	{
		
cout<<"case #"<<i<<": Bad magician!"<<"\n";

	}
	
else

	{

	cout<<"case #"<<i<<": Volunteer cheated!"<<"\n";
	
}


	
	}

	return 0;
}