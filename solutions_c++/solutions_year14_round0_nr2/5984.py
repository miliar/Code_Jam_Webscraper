#include <iostream>
#include <iomanip>
#include <float.h>
using namespace std;

int main() {
	int N;
	cin >> N;
	
	for (int n=1; n<=N;n++) {
		double c,f,x;
		cin >> c >> f >> x;
		
		int maxFramCount = 0;
		double result = DBL_MAX;
		
		double p;
		while(true) {
			double p = 2.0;
			double current_time = 0.0;
			double cookie = 0.0;
			
			for(int i=0;i<maxFramCount;i++) {
				double nextFarmDuration = c / p;
				cookie = 0;
				current_time += nextFarmDuration;
				p += f;
 
				if (cookie > x) {
					goto disp_result;
				}
				
			}
			
			double nextDuration = (x -cookie) / p;
			current_time += nextDuration;
			
			if (current_time<result) {
				result = current_time;
			} else {
				break;
			}

			maxFramCount++;
			
		}
disp_result:
		cout << "Case #" << n << ": " << fixed << setprecision(7) <<result << endl;
	}




}