#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    

	int count,t,item,r1,r2,arr1[4][4],arr2[4][4],r,c;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		count=0,item=0;	
		cin>>r1;
		--r1;
		for(r=0;r<4;r++)
		{	
			for(c=0;c<4;c++)
			{
				cin>>arr1[r][c];
			}
		}
		cin>>r2;
		--r2;
		for( r=0;r<4;r++)
		{	
			for(c=0;c<4;c++)
			{
				cin>>arr2[r][c];
			}
		}
		//Logic Begins Here
		
		for(int a=0;a<4;a++)
		{	
			for(int b=0;b<4;b++)
			{
				if(arr1[r1][a]==arr2[r2][b])
				{
					++count;
					if(count==1)
					{
						item=arr1[r1][a];
					}
					else
						item=0;
				}	
			}
		}
		if(item!=0)
		{
			cout<<"Case #"<<i<<": "<<item<<"\n";
		}
		else
		{
			if(count==0)
				cout<<"Case #"<<i<<": Volunteer cheated!\n";
			if(count>=2)
				cout<<"Case #"<<i<<": Bad magician!\n";

		}
	}
	return 0;
}		
