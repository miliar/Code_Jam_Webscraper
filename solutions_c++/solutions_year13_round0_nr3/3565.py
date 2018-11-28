#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
using namespace std;
long revdig(long n){
	long r = 0;
	while (n!=0){
		long x = n/10;
		r = r*10 + (n-x*10);
		n = x;
	}
	return r;
}
bool ispal(long n){
	return (n==revdig(n))?true:false;
}

int main(){
	ifstream input("input.txt");
	ofstream output;
	output.open("output.txt");
	if (input.is_open()){
		long numcases = -1;
		long casenum = 1;
		while (input.good()){
			string line;
			getline(input, line);
			if (line.size()==0)
				continue;
			istringstream iss(line);
			if (numcases == -1){
				iss>>numcases;
				continue;
			}
			long low, high;
			iss>>low;
			iss>>high;
			long nc = 0;
			for (long x=low; x<=high; x++){
				for (long i=1; i<=x; i++){
					if (i*i>x) break;
					if (i*i==x){
						if (ispal(x)&&ispal(i)) nc++;
						break;
					}
				}
			}
			output<<"Case #"<<casenum++<<": "<<nc<<endl;
		}
		
	}
	input.close();
	output.close();
}

