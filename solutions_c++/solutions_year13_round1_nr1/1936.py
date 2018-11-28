#include<iostream>
#include<string>
#include<cstring>
#include<cmath>
#include<vector>
#include<algorithm>
#include<fstream>

using namespace std;

unsigned long long area(unsigned long long n, unsigned long long r){
	unsigned long long result = (2 * n + 2 * r - 1) * n;
	return result;
}

int main(int argc, const char **argv){
	ifstream input;
	ofstream output;
	input.open(argv[1]);
	output.open(argv[2]);
	if(!input.is_open() || !output.is_open()){
		exit(0);	
	}
	int numcase;
	input >> numcase;
	for(int i = 0; i < numcase; i ++){
		unsigned long long r, t;
		input >> r >> t;
		unsigned long long temp0 = t / r;
		unsigned long long temp1 = sqrt(t / 2) + 1;
		unsigned long long end = temp0;
		if(end > temp1){
			end = temp0;
		}
		unsigned long long start = end / 2;
		unsigned long long mid;
		while(start <= end){
			mid = (start + end) / 2;
			unsigned long long diff0 = area(mid, r);
			unsigned long long diff1 = area(mid + 1, r);
			if(diff0 > t){
				end = mid - 1;
			}
			else if(diff1 <= t){
				start = mid + 1;
			}
			else{
				start = mid;
				end = start - 1;
			}  
		}
		output << "Case #" << i + 1 << ": " << mid << endl;
	}
	input.close();
	output.close();
	return 0;
}
