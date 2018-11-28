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
int ntests, N1, N2;
int a1[4][4], a2[4][4];

ifstream ifs("C:\\Users\\xyz\\Documents\\Visual Studio 2005\\Projects\\mm14\\test.txt");
ifs >> ntests;


ofstream ofs("C:\\Users\\xyz\\Documents\\Visual Studio 2005\\Projects\\mm14\\out.txt");
F(it,0,ntests) {

	ifs >> N1;
	--N1;
	F(i,0,4) F(j,0,4) {
		ifs >> a1[i][j];
	}
	ifs >> N2;
	--N2;
	F(i,0,4) F(j,0,4) {
		ifs >> a2[i][j];
	}

	int res, nres=0;
	F(i,0,4) {
		int x = a2[N2][i];
		if( find( a1[N1], a1[N1]+4, x ) != a1[N1]+4 ) {
			res = x;
			++nres;
		}
	}
		
	if( nres == 1 )
		ofs << "Case #" << it+1 << ": " << res << endl;
	else if( nres > 1)
		ofs << "Case #" << it+1 << ": " << "Bad magician!" << endl;
	else
		ofs << "Case #" << it+1 << ": " << "Volunteer cheated!" << endl;
	
}

ofs.flush();
ofs.close();
return 0;
}
