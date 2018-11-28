#include "cmath"
#include "cstdio"

#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
#include<iostream>
using namespace std;





  int main()

  {

    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
	  
	  int pd[]={1,2,3,4,5,6,7,8,9,11,22,33};
	  int fs[]={1,4,9,121,484};
	  
	  int t;
	  scanf("%d",&t);
	  int a;int b;
	  int d;
	  for (int cas=1;cas<=t;cas++)
	  {
		  d=0;
		 scanf("%d%d",&a,&b);
		 for (int i=0;i<=4;i++)
		 {
			 if ((fs[i]>=a)&&(fs[i]<=b))
				 d++;
		 }
	cout<<"Case #"<<cas<<": "<<d<<endl;
	  }
  
	  
	  return 0;
  }

	  
		


	  





		  


	
	  
	

	  
	  

