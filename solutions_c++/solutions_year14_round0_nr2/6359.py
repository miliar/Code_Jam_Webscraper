#include <iostream>
#include <iomanip>
#include <fstream>

int main() {
	using namespace std;
	
	ifstream in_file("B-large.in");
	ofstream out_file("out-large.txt");
	int test_cases;
	in_file >> test_cases;
	
	
	double c, f, x, 
		t,       // time
		rate,    // rate of cookie production
		cookies; // number of cookies
	
	
	out_file << fixed << setprecision(7);
	
	for(int i = 0; i < test_cases; ++i) {
		out_file << "Case #" << i + 1 << ": ";
		
		in_file >> c >> f >> x;
		
		
		// Rather than adding cookies in a loop, it would be better to do some math
		t    = 0.0;
		rate = 2.0;
		
		double time1, time2;
		
		// if target less than price of farm, it's done from the beginning
		if(x < c) {
			out_file << x / rate;
		} else {		
			while(true) {
				// first, buy the first batch
				t += c / rate;
				
				time1 = (x - c) / rate; 
				time2 = x / (rate + f);
				
				if(time1 < time2) {
					t += time1;
					break;
				}
				rate += f;
			}
			
			out_file << t;
		}
		
		
		out_file << endl;
	}
	
	
	in_file.close();
	out_file.close();
	return 0;
}
