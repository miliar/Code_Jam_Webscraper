#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
using namespace std;
/*
int findindex(int a[],int size,int n)
{
	int beg=0,mid=size/2,end=size-1;
	while(beg>0)
	{
		if(a[i])
	}
	
}*/

int solve(int a[],bool v[],int c,int all,int le)
{
	int left=le;
	int steps=0;
	
	while(left>0)
	{
		int how=0;
		for(int i=0;i<c;i++)
		{
			if(a[i]<all&&v[i])
			{
				v[i]=false;
				all+=a[i];
				how++;
				left--;
			}
		}
		
		if(how==0)
		{
			int v1;
			int v2,st=0;
			int anew1[c],anew2[c];
			bool vnew1[c],vnew2[c];
			
			for(int i=c-1;i>=0;i--){
				if(st==1){
				anew1[i]=a[i];
				vnew1[i]=v[i];
				}
				else{
					if (v[i]){
					anew1[i]=0;
					vnew1[i]=false;
					st=1;}
					else {
						anew1[i]=a[i];
						vnew1[i]=v[i];
						
					}
				}
				anew2[i]=a[i];
				vnew2[i]=v[i];
				
			}	
			//cout<<all<<"    "<<left;
			//cout<<left<<endl;	
			v1= solve(anew1,vnew1,c,all,left-1);
			if(all>1)	
			v2= solve(anew2,vnew2,c,all+all-1,left);
			
			else v2=1000000;
			
			steps = (v1<v2)?v1+1 :v2+1 ;
			break;
		}
	}
	//cout<<"dfgdf\n";
	return steps;
}
int main()
{
	int t;
	cin>>t;
	for(int lo=1;lo<=t;lo++)
	{
		int a,n;
		cin>>a>>n;
		int array[n];
		
		for(int j=0;j<n;j++)
		cin>>array[j];
		
        sort(array, array + n);
        bool v[n];
		
		for(int i=0;i<n;i++)
		v[i]=true;
        
        cout<<"Case #"<<lo<<": "<<solve(array,v,n,a,n)<<endl;
        	
	}
	
	
}
