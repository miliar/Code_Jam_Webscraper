#include <iostream>
#include <fstream>
#include <list>

using namespace std;

int main(int argc,char* argv[])
{
	std::ifstream infile(argv[1]);
	int T;
	infile >> T; //no of testcases

	// variables for each testcase
	int N; 
	list<int> nao;
	list<int> ken;
	list<int>::iterator it_nao,it_ken;
	float temp;
	int tempi;
	int opt;
	int act;


	for (int i=0;i<T;i++)
	{
		//variable intioalization for each testcase
		infile >> N;
		nao.clear();
		ken.clear();
		opt=0;
		act=0;


		for (int j=0;j<N;j++)
		{
			infile >> temp;
			temp *= 100000;
			tempi = (int)temp;
			nao.push_back(tempi);
		}
		for (int j=0;j<N;j++)
		{
			infile >> temp;
			temp *= 100000;
			tempi = (int)temp;
			ken.push_back(tempi);
		}

		nao.sort();
		ken.sort();

		it_nao=nao.begin();
		it_ken=ken.begin();
		while((it_ken!=ken.end()) && (it_nao!=nao.end()))
		{
			if(*it_ken > *it_nao)
			{
				it_ken++;
				it_nao++;
				opt++;
			}
			if(*it_ken < *it_nao)
				it_ken++;

		}
		opt = N - opt;

		while(nao.size()!=0)
		{
			if(*nao.begin() < *ken.begin())
			{
				ken.pop_back();
				nao.pop_front();
			}
			else 
			{
				nao.pop_front();
				ken.pop_front();
				act++;


			}
		}
		cout << "Case #" << i+1 << ": " <<  act << " " << opt << endl;
	}
	return 0;
}

