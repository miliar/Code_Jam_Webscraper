#include<iostream>
#include<fstream>
using namespace std;

double timee(int n,double c,double f);
int main()
{
	
	float base=2;
	double maxsum,sum,tt,c,f,x;
	ifstream in;
	in.open("B-small-attempt0.in");
	ofstream out;
	
	out.open("output.op");
	out.precision(7); 
	out.setf(std::ios::fixed, std::ios::floatfield);
	
	int num_l;
	in>>num_l;

	for(int i=0;i<num_l;i++)
	{
		
		in>>c>>f>>x;
		maxsum=x/2;
		for(int j=1;;j++)
		{
			tt=f*j;
			tt+=2;
			sum=timee(j,f,c);			
			sum+=x/tt;
				
			if(sum<maxsum)			
				maxsum=sum;	
				
			else
			break;
			
			
		}
		out<<"Case #"<<i+1<<": "<<maxsum<<endl;
		
		
	}
	
	
	 	
	return 0;
}

double timee(int n,double c,double f)
{

	double start,cc=2,sum=0;
	
	int i=0;
	while(i<n)
	{
		i++;
		start=f/cc;		
		sum+=start;
		cc+=c;
			
		
	}
	
	return sum;
}
