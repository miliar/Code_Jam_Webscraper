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
#define outr(x,y) fout<<"Case #"<<x+1<<": "<<y<<endl;
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int main(){
	int T;
	fin >> T;
	int N;
	string temp;
	vector<int> count;
	int lns[100][100] = { { 0 } };
	for (int k = 0; k < T; k++){
		fin >> N;
		count.clear();
		vector <char> check;
		vector<char> checktemp;
		for (int z = 0; z < 100; z++){
			for (int y = 0; y <100; y++) lns[y][z] = 1;
		}
		for (int i = 0; i < N; i++){
			int c = 0;
			fin >> temp;
			check.clear();
			for (int m = 0; m < temp.size() - 1; m++){
				if (temp[m] != temp[m + 1]){ check.push_back(temp[m]);  c++; }
				else lns[i][c]++;
			}
			count.push_back(c + 1);
			check.push_back(temp[temp.size()-1]);
			if (checktemp != check && checktemp.size()>0) {count.push_back(1); count.push_back(-1); break;}
			checktemp = check;
		}
		int p;
		for (p = 0; p < count.size(); p++){
			if (count[p] != count[0]){
				outr(k, "Fegla Won");
				break;
			}
		}
		if (p == count.size()){
			int res = 0;
			for (int z = 0; z < count[0]; z++){
				int min = 100;
				int max = 0;
				for (int y = 0; y < N; y++)
				{
					if (lns[y][z] < min) min = lns[y][z];
					if (lns[y][z]>max) max = lns[y][z];

				}
				int mindif = 9999999;
				for (int mm = min; mm <= max; mm++){
					int cc = 0;
					for (int y = 0; y < N; y++)
					{
						cc += abs(mm - lns[y][z]);
					}
					if (cc < mindif) mindif = cc;
				}
				res +=mindif ;
			}
			outr(k, res);
		}

	}

	return 0;
}