#include<iostream>
#include<cstdio>
#include<iomanip>
#include<fstream>
using namespace std;
int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");
	int t;
	double c,f,x,min,curc,t1,pr,t2=0,t3;
	in>>t;
	for(int i=0;i<t;i++)
	{
	in>>c>>f>>x;
	pr=2.0;
	min=0;
	while(1)
	{
		t1=x/pr;
		t2=(c/pr);
		pr=pr+f;
		t3=(x/pr);
		if((t2+t3)<t1)
		min=min+t2;
		else
		{
			min=min+t1;
		    break;
		}
	}
	out<<"Case #"<<i+1<<": "<<fixed<<setprecision(7)<<min<<endl;
    }
    return 0;

}




