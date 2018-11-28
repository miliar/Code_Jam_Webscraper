#include <iostream>
#include <vector>
using namespace std;



int main()
{
	
	int t,t2,i,j,n,m,min;
	bool poss,change;
	cin>>t;
	t2=t;
	while(t2--)
	{
		vector<vector<int> > a(102,vector<int>(102));
		poss=false;
		//input
		cin>>n>>m;
		min=101;
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				cin>>a[i][j];
				if(a[i][j]<min)
					min=a[i][j];
			}
		}
		//input end
		
		while(m!=0 && n!=0)
		{
			change=false;
			//row check
			for(i=0;i<n;i++)
			{
				if(a[i][0]!=min)
					continue;
				for(j=1;j<m;j++)
				{
					if(a[i][j]!=min)
						break;
				}
				if(j==m)
				{
					a.erase(a.begin()+i);
					n--;
					change=true;
					
					break;
				}
			}
				
			//column check
			for(i=0;i<m;i++)
			{
				if(a[0][i]!=min)
					continue;
				for(j=1;j<n;j++)
				{
					if(a[j][i]!=min)
						break;
				}
				if(j==n)
				{
					for(int k=0;k<n;k++) 
					{
					a[k].erase(a[k].begin()+i);
					}	
					m--;
					change=true;
						
					break;		
				}
			}
			min=101;
			for(i=0;i<n;i++)
			{
				for(j=0;j<m;j++)
				{
					if(a[i][j]<min)
						min=a[i][j];
				}
			}
			if(!change)
			 break;	
		}
		
		if(m==0||n==0)
			cout<<"Case #"<<t-t2<<": YES"<<endl;
		else 
			cout<<"Case #"<<t-t2<<": NO"<<endl;
			
	
	}
	
}
