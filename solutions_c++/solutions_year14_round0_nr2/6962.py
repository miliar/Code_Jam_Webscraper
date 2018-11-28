#include <iostream>
using namespace std;
typedef long double LD;
int main()
{
	int t;
	LD c,f,x;
	cout.precision(10);
	cin>>t;
	for(int i=1;i<=t;i++)
	{	
		cin>>c>>f>>x;
		LD s=0,pr=2.0;
		while(((x-c)/pr)>(x/(pr+f)))
		{
			s=s+(c/pr);
			pr=pr+f;
		}
		s=s+(x/pr);
		 cout<<"Case #"<<i<<": "<<s<<"\n";
	}
}