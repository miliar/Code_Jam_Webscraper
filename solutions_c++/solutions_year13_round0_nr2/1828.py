#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<climits>
#include<utility>
#include<cstdlib>
#include<cstring>
using namespace std;
int main()
{
	int t, n , m, a=1;
	scanf("%d", &t);
	while(a<=t)
	{
		int max=0, x, y;
		
		cin>>n>>m;
		int arr[n][m];
		int arry[m], arrx[n]; 
		for(int i=0; i<n ; i++)
		{
			for(int j=0 ; j<m ; j++)
			{
				cin>>arr[i][j];
				if(arr[i][j]>max)
				{
					max=arr[i][j];
					x=i;y=j;
				}
			}		
		}
	//	cout<<x<<" "<<y<<"\n";
	//	cout<<"\n";
		int flag=0;
		
		for(int i=0 ; i<m ; i++)
			arry[i]=max;
		for(int i=0 ; i<n ; i++)
			arrx[i]=max;

		/*for(int i=0 ; i<m ; i++)
			cout<<arry[i]<<" ";
		cout<<"\n";
		for(int i=0 ; i<n ; i++)
			cout<<arrx[i]<<" ";*/
		for(int p=x-1 ; p>=0 ; p--)
		{
			if(arrx[p]>arr[p][y])
			{
				arrx[p]=arr[p][y];
				//cout<<"-1"<<"\n";
			}
		}
		for(int p=x+1 ; p<n ; p++)
		{
			if(arrx[p]>arr[p][y])
			{
				arrx[p]=arr[p][y];
				//cout<<"-1"<<"\n";
			}
		}
		for(int p=y+1 ; p<m ; p++)
		{
			if(arry[p]>arr[x][p])
			{
				arry[p]=arr[x][p];
			}
		}
		for(int p=y-1 ; p>=0 ; p--)
		{
			if(arry[p]>arr[x][p])
			{
				arry[p]=arr[x][p];
			}
		}
		flag=0;
/*		for(int i=0 ; i<m ; i++)
			cout<<arry[i]<<" ";
		cout<<"\n";
		for(int i=0 ; i<n ; i++)
			cout<<arrx[i]<<" ";*/
		for(int i=0 ; i<n ;i++)
		{
			for(int j=0 ; j<m ; j++)
			{
				
				if(arr[i][j]!=min(arrx[i],arry[j] ))
				{
				//	cout<<arrx[i]<<" "<<arry[j]<<"\n";
				//	cout<<i<<" "<<j<<"\n";
					flag=1;
					break;
				}
			}
		}
		if(flag==1)
		{
			cout<<"Case #"<<a<<": NO"<<"\n";
		}
		else	
		{
			cout<<"Case #"<<a<<": YES"<<"\n";	
		}
		a++;
	}

	return 0;
}
