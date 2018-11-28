//Kanish
#include<bits/stdc++.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<limits.h>
#include<vector>
#include<deque>
#include<map>
#include<set>
#include<stack>
#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
long long pow(int a, int b, int MOD)

{

long long x=1,y=a; 

while(b > 0)

{

if(b%2 == 1)

{

x=(x*y);

if(x>MOD) x%=MOD;

}

y = (y*y);

if(y>MOD) y%=MOD; 

b /= 2;

}

return x;

}

int a[1003];
 
void solve()
{
	
            
			  int t;
			  cin>>t;
			   int cases;
			  for(int kkk=1;kkk<=t;kkk++)
			  {
			  	// cases++;
			  	  vector<string> result;
			  	  
			  	   int n;
			  	   cin>>n;
			  	  for(int i=0;i<1005;i++)
			  	  a[i]=0;
			  	  
			  	  for(int j=0;j<10;j++)
			  	  {
					}
			  	   for(int i=0;i<n;i++)
			  	   {
			  	   	  cin>>a[i];
			  	   	  
				   }
				   int xzx=0;
				     for(int j=0;j<10;j++)
			  	  {
			  	  	break;
					}
				 
			for(;;)
				{
				
					    int threesz=0;
					   	int finalx=0;
					    for(int i=0;i<n;i++)
					 threesz+=a[i];	 
					
						if(threesz==0)
						break;
						int mx=0;
						int fin=-1, fx1=-1;
						string nananas="";
						for(int i=0;i<n;i++)
						{
						   	   if(a[i]>mx)
								  {
								  	 mx=a[i];
								  	 fin=i;
								   } 
						}
						int maxiii=0;
						
						
						for(int i=0;i<n;i++)
						{ 
						
						          if(i!=fin && a[i]>maxiii)
						          {
						          	  maxiii=a[i];
						          	  fx1=i;
								  }
						}
						
						
						
							a[fx1]--;
						a[fin]--;
					
						maxiii=0;
					
				 int xzx=0;
				     for(int j=0;j<10;j++)
			  	  {
			  	  	xzx+=j;
			  	  	break;
					}
						for(int i=0;i<n;i++)
						{
						if(a[i]>maxiii)
							   maxiii=a[i];
							   finalx+=a[i];
						}
						
			
						
						if(maxiii>=(finalx/2)+1)
						{
				
							    nananas+=char('A'+fin);
							    a[fx1]++;
							    result.push_back(nananas);
						}
						else
						{
							
							   nananas+=char('A'+fin);nananas+=char('A'+fx1);result.push_back(nananas);
						}
				}
				cout<<"Case #"<<kkk<<": ";
			
			
				for(int i=0;i<result.size();i++)
				cout<<result[i]<<" ";
				cout<<endl;
				
			
			}
			return ;	
}
int main()
{
		freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
         solve();
			return 0;
}
