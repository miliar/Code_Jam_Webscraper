#include <iostream>
#include <sstream>
#include <string>
#include <fstream>
#include <math.h>
#include <iomanip>
#include <limits>

using std::cout;
using std::cin;
using std::string;
using std::stringstream;

// エントリポイント
int main(int argc, char* argv[])
{
	std::ofstream ofs("result.txt");
	ofs.setf(std::ios_base::fixed, std::ios_base::floatfield);
	
	string buf;
	int time(0), n;
	double cost(0.0), farm(0.0), x(0.0), total(0.0);
	cin >> time;
	cin.ignore(1024, '\n');
	
	for ( int t=1; t<=time; t++ ) {
		
		// 1ライン入力
		std::getline(cin, buf);
		stringstream ss(buf);
		ss >> cost >> farm >> x;
		if ( ss.fail() ) return 0;
		
		total = 0.0;
		n = (int)floor(x/cost - 2.0/farm - 1.0 - std::numeric_limits<double>::epsilon());
		if ( n>=0 ) {
			for ( int k=0; k<=n; k++ ) {
				total += cost / (2.0 + k * farm);
			}
			total += x / (2.0 + (n + 1) * farm);
		}
		else {
			total = x / 2.0;
		}
		ofs << "Case #" << t << ": " << std::setprecision(7) << total << "\n";
	}
	
	return 0;
}

