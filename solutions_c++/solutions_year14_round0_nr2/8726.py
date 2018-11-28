#include<fstream>
#include<iostream>
#include <iomanip>

using namespace std;


int main()
{	
	ifstream input;
 	ofstream output;
 	input.open("one.txt");
 	output.open("two.txt");
	int t;
	input>>t;
	int s=t;
	while(t--)
	{   double ans=0.0000000,d=2.0000000,c,f,x,p,q;
	    int flag=0;
	    input>>c;
		input>>f;
		input>>x;
	    while(flag!=1)
	    {p=x/d;
	     q=c/d+x/(d+f);
	     
	     if(p<=q)
	     {ans+=x/d;
	     flag=1;
	     }
	     
	     else
	     ans+=c/d;
	     
	     d+=f;
	     
	    }
	    output <<"Case #"<<s-t<<": "<< std::setprecision(50)<<ans << '\n';
	 
	}
	return 0;
}
