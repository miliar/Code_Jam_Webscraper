#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{ int t,i,j,first,second,same,c=0,val,x;
  scanf("%d",&t);
  while(t--)
   { int check[17]={0};
     
	 same=val=0;
     ++c;
   	 
	 scanf("%d",&first);
   	 for(i=1;i<=4;i++)
		for(j=1;j<=4;j++)
		    {   scanf("%d",&x);
		    	if(i==first)++check[x];
		    }
		    
     scanf("%d",&second);
   	 for(i=1;i<=4;i++)
		for(j=1;j<=4;j++)
		    {   scanf("%d",&x);
		    	if(i==second)
		    	   { if(check[x]==1){ ++same; val=x; }
		    	   }
		    }
		    
	  cout<<"Case #"<<c<<": ";	
	  		
	  if(same==1)cout<<val<<endl;
	  else if(same==0)cout<<"Volunteer cheated!"<<endl;
	  else if(same>1)cout<<"Bad magician!"<<endl;
  }
  return 0;
	
}
