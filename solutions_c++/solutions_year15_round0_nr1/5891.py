#include<iostream>
#include<cstdlib>
#include<string>
#include<sstream>
#include<fstream>

using namespace std;

int main(){

	int N,len;
	char a;
	ifstream f;
	ofstream g;
	f.open("input.txt");
	g.open("output.txt");

	f >> N;

	for(int i=0;i<N;++i){
		f >> len;

		int res=0;
		int sum=0;
		for(int j=0;j<=len;++j){
			f >> a;
			int d = a - '0';
			if(sum<j){
				res+=j-sum;
				sum+=j-sum;
			}
			sum+=d;
		}
		g << "Case #"<<i+1<<": "<<res<<"\n";
	}
	return 0;
}
