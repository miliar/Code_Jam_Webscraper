#include<iostream>
using namespace std;

int num,flag=0;
int check(int a[],int p)
{
	
	if(p==a[0]||p==a[1]||p==a[2]||p==a[3])
	{flag++;
	num=p;
	}
return 0;	
}


int main()
{
	int t,count=0;
	cin>>t;
	int a[4];
	while(t>0)
	{   count++;
		int z,p,x,i,j;
	    flag=0;	
		cin>>x;
		for(int i=0;i<4;i++)
		{
		for(int j=0;j<4;j++)
		{
			
			if(i==x-1)
			{
				cin>>a[j];
			
			}
			else
			{
			cin>>z;	
			}	
		}
		}
	    cin>>x;
	
	    for(int i=0;i<4;i++)
		{
		for(int j=0;j<4;j++)
		{
			
			if(i==x-1)
			{
				cin>>p;
		    
				check(a,p);
				
			}
			else
			{
			cin>>z;	
			}	
		}
		}
	
	
	      
	
	    
	
		if(flag==0)
		cout<<"Case #"<<count<<": "<<"Volunteer cheated!"<<endl;
		else if(flag==1)
		cout<<"Case #"<<count<<": "<<num<<endl;
		else
		cout<<"Case #"<<count<<": "<<"Bad magician!"<<endl;
		
		
		t--;
	}
	
	return 0;
}
