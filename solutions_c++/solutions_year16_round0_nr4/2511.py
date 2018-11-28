#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
using namespace std;

int main(int argc, char* argv[])
{
	string input;
	fstream fin;
	fin.open(argv[1], ios::in);
	getline(fin, input);
	int K, C, S;
	int case_counter = 0;
	while(getline(fin, input))
	{
		++case_counter;
		istringstream ss(input);
		ss>>K>>C>>S;
		cout<<"Case #"<<case_counter<<": ";
		for(int i = 1; i <= K; ++i)
			cout<<i<<" ";
		cout<<endl;
	}
	return 0;
}
