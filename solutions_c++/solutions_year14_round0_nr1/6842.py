 
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main()
{
   int T;
   cin>>T;
   
   for(int l1=0;l1<T;l1++)
   {
	int matchingcount=0,matching, a1, a2;
	int inp[4];
	   
	   
	   cin>>a1;
	   a1--;
	   for(int l2=0;l2<4;l2++)
	   {

		   for(int l3=0;l3<4;l3++)
		   {
			   int temp;
			   cin>>temp;
			   if(l2==a1)
				   inp[l3]=temp;
		   }
	   }
	   cin>>a2;
	   a2--;
	   for(int l4=0;l4<4;l4++)
	   {
		   for(int l5=0;l5<4;l5++)
		   {
			   int temp;
			   cin>>temp;
			   if(l4==a2)
			   {
			   for(int l6=0;l6<4;l6++)
			   {
				   if(inp[l6]==temp)
				   {
					   matching=temp;
					   matchingcount++;
					   
				   }
			   }
			   }
		   }
	   }
	   
	   if(matchingcount==0) cout<<"Case #"<<l1+1<<": Volunteer cheated!"<<endl;
	   else if (matchingcount==1) cout<<"Case #"<<l1+1<<": "<<matching<<endl;
	   else if (matchingcount>1) cout<<"Case #"<<l1+1<<": Bad magician!"<<endl;
	  
   }
    return 0;
}