#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <limits>
#include <vector>
#include <set>
#include <iterator>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstdio>

using namespace std;

class R1P2
{
private:
	long K, A, B, out;
public:
	R1P2();
	void getInput(ifstream& file);
	void eval();
	void dumpOutput(ofstream& file, int TCCnt);
};

R1P2::R1P2()
{
	A = B = K = out = 0;
}

void R1P2::getInput(ifstream& file)
{
	file >> A;
	file >> B;
	file >> K;
}

void R1P2::dumpOutput(ofstream& file, int TCCnt)
{
	std::stringstream ss1;
	ss1 << TCCnt+1;
	std::string compMsg = "Case #"+ss1.str()+": ";
	file.write(compMsg.c_str(), compMsg.length());
	file << out << "\n";
}

void R1P2::eval()
{	
	long i,j,k,res=0;
	for(i=0;i<A;i++)
	{
		for(j=0;j<B;j++)
		{
			k = i&j;
			if(k < K)
				res++;
		}
	}
	out = res;
}

int main()
{
	ifstream file;
	file.open("input.in");
	ofstream fileOut;
	fileOut.open("output.out");
	std::string line;
	getline(file, line);
	int noOfTC = atoi(line.c_str());
	for(int i = 0; i < noOfTC; i++)
	{
		R1P2 t;
		t.getInput(file);
		t.eval();
		t.dumpOutput(fileOut, i);
	}
	file.close();
	return 0;
}