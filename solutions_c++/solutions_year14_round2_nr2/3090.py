#include <iostream>
#include <fstream>
using namespace std;
int main(){
	ifstream fin;
	fin.open("input.in");
	ofstream fout;
	fout.open("output.in");
	int a,b,k,total=0,t;
	fin>>t;
	while(t--){
		fin>>a>>b>>k;
	for (int i = 0; i < a; ++i)
	{
		for (int j = 0; j < b; ++j)
		{
			if((i&j)<k )total++;
		}
	}
	fout<<total<<endl;
	total=0;
	}
}