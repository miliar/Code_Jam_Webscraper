#include <bits/stdc++.h>
#define pf printf
#define sc scanf
using namespace std;
bool bitm[40];
int main()
{
    int t;
    sc("%d", &t);
	while(t--)
	{
		
		int n,j1;
		sc("%d%d", &n, &j1);
		int cnt=0;
		int start=4;
		int s1=6;
		pf("Case #1:\n");
		while(cnt<j1)
		{
			if(cnt==0)
			{
				int i=2;
				bitm[n-1]=bitm[n-2]=bitm[1]=bitm[0]=1;
				while(i<n-3)
				{
					bitm[i+1]=true;		bitm[i]=true;
					
					for(int j=n-1;j>=0;j--)
					cout<<bitm[j];
					
					cout<<" ";
					for(int k=2;k<=10;k++)
					cout<<k+1<<" ";
					bitm[i+1]=bitm[i]=false;
					cnt++;i++;
					cout<<"\n";
				}
			}
			else if(cnt<352)
			{
				int x=start,y=2;
				bitm[n-1]=bitm[n-2]=bitm[1]=bitm[0]=1;
				
				while(x<n-3)
				{
				   bitm[x+1] = bitm[x] = bitm[y+1] = bitm[y] = 1;
				   
				   for(int j=n-1;j>=0;j--)
					cout<<bitm[j];
					
					cout<<" ";
					for(int k=2;k<=10;k++)
					cout<<k+1<<" ";
					
					bitm[x+1] = bitm[x]	= bitm[y+1] = bitm[y]=0;
					cnt++; 
					if(cnt>=j1)
					    break;
					pf("\n");
					x++;   y++;
				}
				start++;
			}

		   else 
		   {
		   	   bitm[n-1] = bitm[n-2] = bitm[2] = bitm[1] = bitm[0] = 1;
		   	   int x=s1,y=4;
		   	    while(x<n-3)
				{
				   bitm[x+1]=bitm[x]=bitm[y+1]=bitm[y]=1;
				   for(int j=n-1;j>=0;j--)
						cout<<bitm[j];
					pf(" ");
					
					for(int k=2;k<=10;k++)
					cout<<k+1<<" ";
					
					bitm[x+1]=bitm[x]	=bitm[y+1]=bitm[y]=0;
					cnt++;
					
					if(cnt>=j1)
					    break;
					pf("\n");
					x++;y++;
				}
				s1++;
		   }	
		}
	}	
}
