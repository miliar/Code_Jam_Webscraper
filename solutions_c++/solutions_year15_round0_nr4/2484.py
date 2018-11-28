#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;



int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    cin>>t;

   for(int i=0;i<t;i++)
   {
	  int X,R,C;
	  cin>>X>>R>>C;
	  if(C<R)
	  {
		  swap(R,C);
	  }

	  if(X==1)
	  {
		   cout<<"Case #"<<(i+1)<<": GABRIEL\n";

	  }
	  else if((C*R)%X>0||X>max(C,R))
	  {
		   cout<<"Case #"<<(i+1)<<": RICHARD\n";

	  }
	  else
	  {
		  if((R==1||R==2)&&C==4&&X==4)
		  {
		   cout<<"Case #"<<(i+1)<<": RICHARD\n";
		  }
		  else if(C==3&&R==1&&X==3)
		  {
			  cout<<"Case #"<<(i+1)<<": RICHARD\n";

		  }
		  else
		  {
			   cout<<"Case #"<<(i+1)<<": GABRIEL\n";

		  }
	  }





   }



    return 0;

}


