#include<iostream>
#include<string>
#include<cstring>
#include<vector>
#include<algorithm>
#include<cassert>
using namespace std;
inline
int min(int a, int b) {
   return a < b ? a : b;
}
int EditDistanceRecursion(const char *X, const char *Y, int m, int n ,int i,int j)
{
	
int left=0;
int right=0;
    if(i<m-1 && j<n-1 )
    {	
 
    
    
    
   
    	if(X[i]!=Y[j])
    	{
    		if(Y[i-1]==Y[i] && X[i]==Y[i+1])
    		{	 left= 1+ EditDistanceRecursion(X,Y,m,n,i+1,j+2);}
    		if(X[i-1]==X[i] && Y[i]==X[i+1])
    		{	right= 1+ EditDistanceRecursion(X,Y,m,n,i+2,j+1);}
    	}	
    	
   
 cout<<left<<right<<endl;
    return min(left, right);
	}
	return 0;
}
int main()
{
	int T;
	cin>>T;
	for(int t=0;t<T;t++)
	{
		int count=0;
		int a,b,k;
		cin>>a>>b>>k;
		
		for(int i=0;i<a;i++)
		{
			for(int j=0;j<b;j++)
			{	
				if((i&j) < k)
				{
					count++;
					
				}	
			}	
		}		
		
			cout<<"Case #"<<t+1<<": "<<count<<endl;
    	
	}
	return 0;
}