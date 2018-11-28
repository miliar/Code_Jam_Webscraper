#include   <fstream>
#include   <iomanip>
#include   <algorithm>
#include   <cstring>
#include   <sstream>
#include   <vector>
#define	   LIMIT 1000
using namespace std;
int main(int argc, char *argv[])
{
	string infpath="B-large.in";
	string outfile="B-large.out";
	string Template="Case #";
	int N;
	double C,F,X;
	ifstream inf(infpath.c_str(),ifstream::in);
	ofstream ouf(outfile.c_str(),ofstream::out);
	inf>>N;
	for(int Case=0;Case<N;Case++)
	{
		inf>>C>>F>>X;
		double prew,w,Time=0.0;
		prew=w=2;
		while(1)
		{
			w=prew+F;
			if(X<C)
			{
			  Time=X/prew;
			  break;
			}
			else
			{
				if((X-C)/prew>(X/w))
				  Time+=C/prew;
				else
				{
				  Time+=X/prew;
				  break;
				}
				prew=w;
			}
		}
		ouf<<Template<<(Case+1)<<": "<<fixed<<setprecision(7)<<Time<<endl;
	}
	inf.close();
	ouf.close();
	return 0;
}





