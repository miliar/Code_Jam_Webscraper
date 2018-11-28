#include<iostream>
#include<vector>
#include<utility>
#include<limits.h>
#include<set>
#include<map>
#include<algorithm>
using namespace std;

int a[4][4];
int b[4][4];

int main()
{
	freopen("outA.txt","w",stdout);
	
	int cases;
	cin>>cases;
	int c = 1;
	while(cases--)
	{
		int r1;
		cin>>r1;
		r1--;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			cin>>a[i][j];
			
		int r2;
		cin>>r2;
		r2--;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			cin>>b[i][j];
		
		int ans ;
		int found= 0;
		
		for(int j1=0;j1<4;j1++)
		{
			for(int j2=0;j2<4;j2++)
			{
				if(a[r1][j1] == b[r2][j2])
				{
					ans = a[r1][j1];
					found++;
					break;
				}
			}
			if(found>1)
			break;
		}
		
		if(found==1)
		{
			cout<<"Case #"<<c<<": "<<ans<<endl;
		}
		else if(found>1) 
		{
			cout<<"Case #"<<c<<": Bad magician!\n";
		}
		else if(found == 0)
		{
			cout<<"Case #"<<c<<": Volunteer cheated!\n";
		}
		c++;
	}
	return 0;
}


