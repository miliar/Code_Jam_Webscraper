#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

int main()
{

    freopen("a1.in", "r", stdin);
    freopen("a1.out", "w", stdout);
    int n;
    cin>>n;
    
	    
    for(int k=0;k<n;k++)
    {
    	int a[4][4],b[4][4];
    	int r1=0;
    	int r2=0;
    	cin>>r1;
    	for(int i=0;i<4;i++)
    	{
    		for(int j=0;j<4;j++)
    		{
    			cin>>a[i][j];
    		}
    	}

    	cin>>r2;
    	for(int i=0;i<4;i++)
    	{
    		for(int j=0;j<4;j++)
    		{
    			cin>>b[i][j];
    		}
    	
		}
		r1=r1-1;
		r2=r2-1;
		int count=0,num=0;
/*		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(a[r1][i]==b[r2][j])
				{
					count++;
					num=a[r1][j];
				}
			}
		}
		*/
		int ab[20];
		for(int i=0;i<20;i++)
		{
			ab[i]=-1;
		}
		for(int i=0;i<4;i++)
		{
			ab[a[r1][i]]=0;
		}
		for(int i=0;i<4;i++)
		{
			if(ab[b[r2][i]]==0)
			{
				count++;
				num=b[r2][i];
			}
		}		
		
		printf("Case #%d: ", k+1);
		if (count==1)
		{
			cout<<num<<"\n";
		}
		else if(count==0)
		{
			cout<<"Volunteer cheated!"<<"\n";
		}
		else
		{
			cout<<"Bad magician!"<<"\n";
			
		}






    }
    
}
