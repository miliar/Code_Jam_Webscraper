#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iomanip>
#include <algorithm>
#include <functional>
#include <sstream>


using namespace std;

int main(){
	std::ifstream ifs("B-small.in");
	std::ofstream ofs("result.txt");

	int T,A,B,K;
	
	ifs >> T;

	for(int t=1;t<=T;t++){
		ifs>>A;
		ifs>>B;
		ifs>>K;
		int count=0;
		int tmp;
		for(int i=0;i<A;i++){
			for(int j=0;j<B;j++){
				tmp = i&j;

				if(tmp <K){
					count++;
				}

			}
		}
		

		ofs<<"Case #"<<t<<": "<<count<<endl;
	}

}