#include<iostream>
#include<fstream>

#define pi 3.141592653589793

using namespace std;

int main()
{
	long long t,r,ans=1,T;
	long long a,aa=0;

	ifstream in("A-small-attempt1.in");
	ofstream out("output.out");

	in>>T;
	

	while(aa<T)
	{
		in>>r>>t;
		a =((2*r) + 1);
		t-=a;
		
		//cout<<t<<"\n";
		while(t>=a)
		{a+=4; t-=a; 
		if(t>=0) ans++;}
		out<<"Case #"<<(aa+1)<<": "<<ans<<"\n";
		ans=1;
		aa++;
	}
	in.close();
	out.close();
	return 0;


}
	