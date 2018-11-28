#include <math.h> 
#include <algorithm> 
#include <string> 
#include <vector> 
#include <map> 
#include <set> 
#include <sstream> 
#include <iostream> 
#include <ctype.h> 
#include <list>
#include <queue>
#include <numeric>
#include <fstream>

using namespace std; 

#define VS vector<string> 
#define VI vector<int> 
#define VD vector<double>

#define F(v,s,e) for( int v = (int)(s); v < (int)(e); ++v ) 
#define SET00(x) memset( (x), 0, sizeof(x));
#define SETFF(x) memset( (x), 0xff, sizeof(x));

#define ISS istringstream 
#define OSS ostringstream 

#define i64 long long
#define VI64 vector<i64>

const double PI = 4*atan(1.); 
const double EPS = 1.E-12;

const int UP=0, RIGHT=1, DOWN=2, LEFT=3;




int main(int argc, char* argv[])
{   
vector<string> board;
int ntests;
double C,F,X;

ifstream ifs("C:\\Users\\xyz\\Documents\\Visual Studio 2005\\Projects\\mm14\\test.txt");
ifs >> ntests;


ofstream ofs("C:\\Users\\xyz\\Documents\\Visual Studio 2005\\Projects\\mm14\\out.txt");
F(it,0,ntests) {

	ifs >> C >> F >> X;
	ofs.precision(12);

	int tf=1, done=0;
	double prod = 2.;
	double besttime =  X / prod;
	while(!done) {
		double time = 0.;
		prod = 2.;
		F(f,1,tf) {
			double timefarm = C / prod;
			time += timefarm;
			prod += F;
		}
		double timereq = time + X / prod;
		if( timereq > besttime )
			break;
		besttime = timereq;
		++tf;
	}

	ofs << "Case #" << it+1 << ": " << besttime << endl;
	
}

ofs.flush();
ofs.close();
return 0;
}
