#include<fstream>
using namespace std;

int main(int argc, char *argv[])
{
	int t;
	ifstream ip;
	ip.open(argv[1]);
	
	ofstream op;
	op.open("B-output.txt");
	
	ip>>t;
	
	for(int iter=1; iter<=t; iter++)
	{
		op<<"Case #"<<iter<<": ";
		
		double c, f, x;
		ip>>c>>f>>x;
		
		double old_overhead, old_time;
		double overhead, time;
		
		old_overhead = 0;
		old_time = x/2 + 1;
		
		overhead = 0;
		time = x/2;
		
		int num_farm=0;
		while((old_overhead+old_time) > (overhead+time))
		{
			old_overhead = overhead;
			old_time = time;
			
			num_farm++;
			
			overhead = old_overhead + c/(2+(num_farm-1)*f);
			time = x/(2+num_farm*f);
		}
		
		op.precision(14);
		op.setf(ios::fixed);
		op.setf(ios::showpoint);
		
		op<<old_overhead+old_time<<endl;
	}
	return 0;
}
	