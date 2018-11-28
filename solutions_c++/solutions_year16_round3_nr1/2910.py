#include<bits/stdc++.h>
using namespace std;
#define ll long long int
char ans[10000][2]; 
int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("a.out","w",stdout);
	int n,i,t,ti,j;
	cin>>t;
	for(ti=1;ti<=t;ti++)
	{
		cout<<"Case #"<<ti<<": ";
		int arr[27];
		cin>>n;
		int pos=0;
		int max=0;
		for(i=0;i<n;i++)
		{
			cin>>arr[i];
		
			if(max<arr[i])
			{
			
				max=arr[i];
				pos=i;
			}
		}
		char ele=0;
		//odd even
		
		
			int k=0;
			
			for(i=0;i<n;i++)
			{
				if(i==pos)
				continue;
				
				for(j=0;j<arr[i];j++)
				{
					k++;
					
					if(k>max)
					{
						
						cout<<(char)(65+i)<<" ";
					}
					else
					{
						ans[ele][0]=(char)(65+pos);
						ans[ele++][1]=(char)(65+i);
					}
					
				}
			}
	 	for(j=0;j<ele;j++)
		 {
		 	
		 	cout<<(char)ans[j][0]<<(char)ans[j][1]<<" ";	
		}	
		cout<<endl;
	}
	return 0;
}
