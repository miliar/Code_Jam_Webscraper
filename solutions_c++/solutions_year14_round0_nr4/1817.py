#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
using namespace std;

int playWar(vector<double >& nao, vector<double>& ken )	{
	int kend = ken.size()-1;
	int kstart = 0;
	int naoend = nao.size()-1;
	//int naostart = 0;
	int score = 0;
	for ( int i = 0; i < nao.size(); ++i)	{
		//cout<<"nao "<<nao[naoend]<<" ken "<<ken[kend]<<endl;
		if (nao[naoend] > ken[kend])	{
			kstart++;
			score++;
		}
		else	
			kend--;
		naoend--;
	}
	return score;

}

int playDeceifulWar(vector<double>& nao, vector<double>& ken)	{
	int kend = ken.size()-1;
	int kstart = 0;
	//int naoend = nao.size()-1;
	int naostart = 0;
	int score = 0;
	for ( int i = 0; i < nao.size(); ++i)	{
		if (nao[naostart] > ken[kstart])	{
			score++;
			kstart++;
		}
		else
			kend--;
		naostart++;
	}
	return score;

}

int main()	{

	double N = 0;
	int testcase = 0;
	string str;
	getline(cin, str);
	stringstream(str) >> testcase;
	vector< vector<double> > matrix;
	int line = 0;
	while (getline(cin, str))
	{
		stringstream sst(str);
		//cout<<str<<endl;
		if (line%3!=0)	{
			matrix.push_back(vector<double>());
			while (sst.good())	{
				sst>>N;
				matrix.back().push_back(N);

			}
			sort(matrix.back().begin(), matrix.back().end());
		}
		line++;
	}
	//cout.precision(7);
	//cout<< std::fixed;
	for ( int i = 0; i < testcase; ++i)	{
		
		cout<<"Case #"<<i+1<<": "<<playDeceifulWar(matrix[2*i], matrix[2*i+1])<<" "<<playWar(matrix[2*i], matrix[2*i+1])<<endl;;
		
	}

	return 0;
}