#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
#include<string>
#include<climits>
#include<stack>
#include <iomanip>      // std::setprecision
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");
vector <double> na,na1, ke,ke1;

int fair(){
	int count = 0;
	int p = 0;
	for (int i = 0; i < na.size(); i++)
	{
		p = 0;
		for (int k = 0; k < ke.size(); k++)
		{
			if (ke[k]>na[i]) {
				ke.erase(ke.begin() + k);
				p++;
				break;
			}
		}
		if (p == 0){ ke.erase(ke.begin()); count++; }
	}
	return count;
}

int unfair(){
	vector<double> temp;
	temp = ke1;
	ke1 = na1;
	na1= temp;
	int count = 0;
	int p = 0;
	for (int i = 0; i < na1.size(); i++)
	{
		p = 0;
		for (int k = 0; k < ke1.size(); k++)
		{
			if (ke1[k]>na1[i]) {
				ke1.erase(ke1.begin() + k);
				p++;
				break;
			}
		}
		if (p == 0){ ke1.erase(ke1.begin()); count++; }
	}
	return count;

}

int main(){
	int T, N;
	fin >> T;
	
	double temp;
	for (int k = 0; k < T; k++)
	{
		na.clear();
		ke.clear();
		fin >> N;
		for (int i = 0; i < N; i++){
			fin >> temp;
			na.push_back(temp);
		}
		for (int i = 0; i < N; i++){
			fin >> temp;
			ke.push_back(temp);
		}

		sort(na.begin(), na.end());
		sort(ke.begin(), ke.end());
		na1 = na;
		ke1 = ke;
		fout << "Case #" << k + 1 << ": " <<N- unfair() << " " << fair() << endl;
	}

	return 0;
}