#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
using namespace std;
ifstream fin("B-small-attempt0.in");
#define MAX 1000000

int A, B, K;

void process(int t){
	fin>>A>>B>>K;
	int n = 0;
	for(int i=0;i<A;i++)
		for(int j=0;j<B;j++)
		{
			int f = i&j;
			if(f<K)
				n++;
		}
	cout<<"Case #"<<t<<": "<<n<<endl;
}

int main() {
	int T;
	fin>>T;
	for(int i=1;i<=T;i++)
		process(i);
	return 0;
}
