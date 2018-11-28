#include "math.h"
#include "iostream"
#include "fstream"
#include "vector"
#include "string"
#include "set"
#include "unordered_set"
#include "stack"
#include <iomanip>
using namespace std;


int main(){
	int T;
	ifstream in("inputs.txt");
	ofstream out("output.txt");
	in>>T;
	for(int i=0;i<T;i++){
		int K,C,S;
		in>>K>>C>>S;
		out<<"Case #"<<i+1<<": ";
		for(int k=0;k<K;k++){
			out<<setprecision(18)<<k*pow(K,C-1)+1<<" ";
		}
		out<<endl;
	}
}
