#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int n,i,j,k;
double c,f,x,s1,s2,s,t,tmp = 2.0;

int main(int argc, char **argv)
{
	ifstream test;
	test.open (argv[1]);
	ofstream odp;
	odp.open (argv[2]);
	test >> n;
	for (i=0; i<n; i++) {
		test >> c >> f >> x;
		s2 = 0; s1 = 0; s = 0;
		t = 2.0;
		s1 = x/t;
		while (1) {
			s2 += c/t;
			t += f;
			tmp = x/t;
			if (s1 <= (s2 + tmp)) {
				s = s1;
				break;
			} else {
				s1 = s2 + tmp;	
			} 
		}
		odp << "Case #" << i+1 << ": " << setprecision(7) << fixed << s << endl;	
	}

	odp.close();
	test.close();
	
	return 0;
}	
