#include<iostream>
#include<fstream>
using namespace std;
double room(int n,double c,double f);
int main()
{
	ifstream in;
	in.open("B-large.in");
	ofstream out;
	out.precision(7); out.setf(std::ios::fixed, std::ios::floatfield);
	
	out.open("larg.op");
	
	int n;// # case
	in>>n;
	double c,f,x;
	float base=2;
	
	double maxsum;
	
	double sum;
	double tact;
	for(int i=0;i<n;i++)
	{
		
		in>>c>>f>>x;
		maxsum=x/2;
		for(int j=1;;j++)
		{
		tact=f*j;
		tact+=2;
		sum=room(j,f,c);
		
		sum+=x/tact;
			
		if(sum<maxsum)
		{
			//cout<<sum<<endl;
		maxsum=sum;	
			
		}
		else
		break;
			
			
		}
		out<<"Case #"<<i+1<<": "<<maxsum<<endl;
		//printf("%.7f\n",maxsum);
		
	}
	
	
	 
	
	
	return 0;
}

double room(int n,double c,double f)
{

	double start;
	double cc=2;
	double sum=0;
	
	for(int i=0;i<n;i++)
	{
		start=f/cc;
		//cout<<start<<endl;
		sum+=start;
		cc+=c;
			
		
	}
	
	return sum;
}
