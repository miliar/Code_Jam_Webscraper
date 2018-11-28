#include <iostream>
#include <fstream>
#include <string>

int main(int argc, char* argv[])
{
	using namespace std;
	
	int time, s_max, sum, n, x(0);
	string buf;
	
	ifstream ifs(argv[1]);
	ifs >> time;
	
	for ( int t=1; t<=time; t++ ) {
		ifs >> s_max;
		ifs.ignore(1);
		std::getline(ifs, buf);
		
		if ( buf[0]=='0' ) {
			x = 1;
			sum = (buf[0] - '0') + 1;
		}
		else {
			x = 0;
			sum = buf[0] - '0';
		}
		
		for ( int s=1; s<buf.size(); s++ ) {
			n = buf[s] - '0';
			if ( n>0 && sum<s ) {
				x += s - sum;
				sum += s - sum;
			}
			sum += n;
		}
		
		printf("Case #%d: %d\n", t, x);
	}
	return 0;
}

