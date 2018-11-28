#include <iostream>
#include <fstream>
using namespace std;

int main(void)
{
	ifstream fin;
	fin.open("B-small-attempt0.in");
	ofstream fout;
	fout.open("B-small-attempt0.out");
	
	int t;
	fin>>t;
	
	int a,b,k;
	for(int i=0;i<t;i++)
	{
		fin>>a>>b>>k;
		int ret=0;
		for(int m=0;m<a;m++){
			for(int n=0;n<b;n++){
				if((m&n)<k) ret++; 
			}
		}
		fout<<"Case #"<<i+1<<": ";
		fout<<ret<<endl;
		
		
		
	}
	return 0;
}