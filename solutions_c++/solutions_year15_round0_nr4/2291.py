#include<fstream>
#include<string>
#include<math.h>
//#include<algorithem>
using namespace std;
main()
{
	ifstream input("D-small-attempt2.in");
	ofstream output("out.txt");
	int r;
	input>>r;
	
	for(int i=1;i<=r;i++)
	{
	int x,w,b;
	input>>x>>w>>b;
	int z=w*b,f=0;
	int ma=max(w,b);
	int min1=min(w,b);
	int ha1;
	if(x%2==0)
	ha1=x/2;
	else
	ha1=x/2+1;
	if(z%x!=0||x>ma||ha1>min1||(x==4&&3>min1))
	f=1;
	if(f==1)
	output<<"Case #"<<i<<": RICHARD"<<endl;
	else
	output<<"Case #"<<i<<": GABRIEL"<<endl;	
	}
	
}