#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;



int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    cin>>t;
   for(int i=0;i<t;i++)
   {

	   int S;
	   string Smax;
	   cin>>S>>Smax;
	   int peeps=0;
	   int people=0;
	   for(int i=0;i<S;i++)
	   {
		   people+=Smax[i]-'0';
		   while(people<(i+1))
		   {
			   peeps++;
			   people++;
		   }


	   }
	   cout<<"Case #"<<(i+1)<<": "<<peeps<<"\n";
   }



    return 0;

}


