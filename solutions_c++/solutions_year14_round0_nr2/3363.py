#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
	ifstream fin("C://Users/dmx/Desktop/B-large.in");
	ofstream fout("C://Users/dmx/Desktop/answer.txt");	
	int t,  i;
	double c, f, x, sum, left, rate;
	fin>>t;
	for(i = 0; i < t; i++)
	{
		rate = 2;
		sum = 0;
		fin>>c>>f>>x;
		sum += c/rate;
		left = x - c;
		while(left/rate > x/(rate + f) )
		{
			rate += f;
			sum += c/rate;
		}
		sum += left/rate;
		fout<< "Case #"<<i+1<<": "<< fixed << setprecision(7)<<sum<<endl;
		fout.unsetf( ios::fixed ); 
	}
	fout.close();
	fin.close();
	return 0;
}