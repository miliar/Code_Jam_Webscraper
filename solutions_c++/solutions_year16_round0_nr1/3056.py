#include "math.h"
#include "iostream"
#include "fstream"
#include "vector"
#include "string"
#include "set"
#include "unordered_set"
using namespace std;

void fill(unordered_set <int> & rec, long X){
	while(X>0){
		int digit;
		digit=X%10;
		if(rec.find(digit)==rec.end()){
			rec.insert(digit);
		}
		X=X/10;
	}
}

int main(){
	int T;
	ifstream in("inputl.txt");
	ofstream out("output.txt");
	in>>T;
	for(int i=0;i<T;i++){
		out<<"Case #"<<i+1<<": ";
		long N;
		in>>N;
		if(N==0){
			out<<"INSOMNIA"<<endl;
			continue;
		}
		unordered_set <int> rec;
		int rep=0;
		for(rep;rep<10000;rep++){
			long step=(rep+1)*N;
			fill(rec,step);
			if(rec.size()==10){
				out<<step<<endl;
				break;
			}
		}
		if(rep==10000&&rec.size()<10){
			out<<"INSOMNIA"<<endl;
		}
	
	}
}
