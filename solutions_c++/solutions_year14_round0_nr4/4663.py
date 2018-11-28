#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <set>
#include <iterator>
#include <cstring>
#include <climits>
#include <cstdlib>
#include <cstdio>

using namespace std;

double EPS = 1E-8;

string inFile = "D-large.in";
string outFile = "D-large.out";
FILE* in = NULL;
FILE* out = NULL;

int calcDeWarScore(vector<double> Nao, vector<double> Ken)
{
	int score = 0;
	int size = Nao.size();
	while(Nao.size())
	{
		if(Nao[0]>Ken[0]){
			score++;
			Nao.erase(Nao.begin());
			Ken.erase(Ken.begin());
		}
		else{
			Nao.erase(Nao.begin());
			Ken.pop_back();
		}
		if(Nao.size()==0)
			break;
		if(Nao[Nao.size()-1]>Ken[Ken.size()-1]){
			score++;
			Nao.pop_back();
			Ken.pop_back();
		}
		else{
			Nao.erase(Nao.begin());
			Ken.pop_back();
		}
	}
	return score;
}

int calcWarScore(const vector<double>& Nao, vector<double> Ken)
{
	int score = 0;
	vector<double>::iterator iter;
	for(int i=0; i<Nao.size(); i++)
	{
		iter = Ken.begin();
		while(iter!=Ken.end() && *iter<Nao[i])
			iter++;
		if(iter==Ken.end()){
			score++;
			Ken.erase(Ken.begin());
		}
		else
			Ken.erase(iter);
	}
	return score;
}

int main()
{
	if( !( in = fopen(inFile.c_str(), "r") ) )
		exit(-1);
	if( !( out= fopen(outFile.c_str(), "w") ) ){
		fclose(in);
		exit(-1);
	}

    int T;
	fscanf(in, "%d", &T);
	int N;
	double tmp;
	int warScore, deWarScore;
	for(int t=0; t<T; t++)
	{
		fscanf(in, "%d", &N);
		vector<double> Nao;
		vector<double> Ken;
		for(int n=0; n<N; n++){
			fscanf(in, "%lf", &tmp);
			Nao.push_back(tmp);
		}
		for(int n=0; n<N; n++){
			fscanf(in, "%lf", &tmp);
			Ken.push_back(tmp);
		}
		sort(Nao.begin(), Nao.end());
		sort(Ken.begin(), Ken.end());

		warScore = calcWarScore(Nao,Ken);
		deWarScore = calcDeWarScore(Nao, Ken);
		fprintf(out, "Case #%d: %d %d\n", t+1, deWarScore, warScore);
		fflush(out);
	}

	fclose(in);
	fclose(out);
	return 0;
}
