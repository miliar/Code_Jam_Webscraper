#include "iostream"
#include "string"
#include "fstream"

using namespace std;

int main(){
	int T;
	ifstream fin;
	ofstream fout;
	fin.open ("A-large.in");
	fout.open ("small.out");
	fin>>T;
	for (int t=0;t<T;t++) {
		int *sum,l,i;
		string x;
		fin>>l;
		l+=1;
		fin>>x;
		sum = new int[l];
		int acc = 0;
		for (i=0;i<l;i++) {
			sum[i] = acc;
			acc += x[i]-'0';
		}
		int diff =0;
		for (i=0;i<l;i++) {
			if(i-sum[i]>diff)
				diff = i-sum[i];
		}
		fout<<"Case #"<<t+1<<": "<<diff<<endl;
	}
	return 0;
}
