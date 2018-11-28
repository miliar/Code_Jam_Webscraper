#include<string>
#include<vector>
#include<iostream>
#include<algorithm>
#include<fstream>

using namespace std;

int main(){
	ifstream ifs("B-small-attempt0.in");
	ofstream ofs("output.out");
	int numC;
	ifs>>numC;
	for(int g = 0; g<numC; g++){
		long long A, B, K, res = 0;
		ifs>>A>>B>>K;
		
		//res += K * K;
		for(long long i = 0; i<A; i++)
			for(long long j = 0; j<B; j++){
				if( (i & j) < K)res++;
			}

		ofs<<"Case #"<<g+1<<": "<<res<<endl;
		
	}
	system("pause");

}