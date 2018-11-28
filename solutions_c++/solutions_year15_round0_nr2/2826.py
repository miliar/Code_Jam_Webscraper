#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<vector>
#include<set>
#include<math.h>
#include<map>
#include<algorithm>
#include<queue>
#include<cstring>
#include<stack>
using namespace std;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,id=1;;
	cin>>t;
	while(t--)
    {
    	int n,mx=0;
    	cin>>n;
    	int A[1099];
    	for(int i=0;i<n;i++)
    	{
    		cin>>A[i];
    		mx=max(mx,A[i]);
		}
		int req=987654321;
		for(int i=1;i<=mx;i++)
		{
			int tot=i;
			for(int j=0;j<n;j++)
			{
				if(A[j]<=i)
				continue;
				else 
				{
					int rem = A[j]-i;
					int ss = rem/i;
					if(rem%i!=0)
					ss++;
					tot+=ss;
				}
			}
			req=min(req,tot);
		}
    	
    	
    	cout<<"Case #"<<id<<": "<<req<<endl;
    	id++;
	}
	return 0;
}
