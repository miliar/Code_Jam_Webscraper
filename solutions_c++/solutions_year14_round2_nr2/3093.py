// stack::empty
#include <iostream.h>
#include <stack>
#include<fstream>
#include <algorithm>

void re(int *a,int *b,int n,int sp,int k);

long int d_to_b(int x);

using namespace std;
int const x =4;

 //int a[x]={0,1,2,3,4};


int c=0;
int sol[2];

int am,bm;

int b[2];		
 
 int m;
int main ()
{
	
	int n;
	
	ifstream in;
	in.open("B-small-attempt1.in");
	
	ofstream out;
	out.open("output.txt");
	
  
  int bb,a,k; 
  in>>n;
  
  
  
  int nn=0;
 
  

 	 for(int i=0;i<n;i++)
	{
		c=0;
		
		in>>a>>bb>>k;
		bm=bb;
		am=a;
		
		m=max(a,bb);
		
		
		int arr[m];
		
		for(int j=0;j<m;j++)
		{
			arr[j]=j;	
			//cout<<arr[j]<<endl;
		}
		
		re(arr,b,nn,2,k);
		
		
		out<<"Case #"<<i+1<<": "<<c<<endl;
		
	}
	out.close();
  
  
  
  
 
		
  return 0;
}









void re(int *a,int *b,int n,int sp,int k)
{
	int i=0;
	int f=1;
	int y;
	if(n==sp)
	{
		
			if(b[0]>=am )
			return; 
			
			if( b[1]>=bm )
				return; 
			
		//	cout<<b[0]<<" "<<b[1]<<endl;;
			int z=b[0]&b[1];
			//cout<<"xzz"<<z<<endl;
			if(z<k)
			c++;
		
	
	
	
	
	
	}
	else if(n<sp)
	{
		for(i=0;i<m;i++)
		{
			y=a[i];
			f=1;
			
			
			/*for(int j=0;j<n;j++)
			{
				if( y<b[j])
				{
					f=0;
					break;
				}
			}*/
			if(f==1)
			{
				b[n]=y;
				re(a,b,n+1,sp,k);
				
			}
			
			
			
		}
	}
	
	
	
}

