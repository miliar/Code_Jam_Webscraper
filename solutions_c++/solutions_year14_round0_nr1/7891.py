#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
#include <string>
#include <fstream>
#include <iomanip>
using namespace std;

int n,N;
string ans;
//9.10 - 9.54
bool small=false;
string challenge="A";
string empty;

ifstream fin(""+challenge+"-small-0.in");
ofstream fout(""+challenge+"-small-0.out");
ofstream fdbg(challenge+".debug");

int r1, r2;
int row1[4];
int row2[4];

int main(){

	fin >> n;
	//cout << n;
	getline(fin,empty);
	fdbg<<n<<endl;
	
	for(N=1; N<=n; N++){
		int e;
		fin >> r1;
		for(int i = 0; i<4; i++){
			
			for(int j = 0; j<4 ;j++){
				if(i+1 != r1)
					fin >> e;
				else
					fin >> row1[j];
			}
		}

		fin >> r2;
		for(int i = 0; i<4; i++){
			for(int j = 0; j<4 ;j++){
				if(i+1 != r2)
					fin >> e;
				else
					fin >> row2[j];
			}
		}

		set<int> res;

		for(int i = 0; i<4; i++){
			for(int j = 0; j<4; j++){
				if(row1[i]==row2[j])
					res.insert(row1[i]);
			}
		}

		
		if(res.size()==0){
			
			fout << "Case #"<<N<<": "<< "Volunteer cheated!"<<endl;
			cout << "Case #"<<N<<": "<<  "Volunteer cheated!"<<endl;
		} else if(res.size()==1){
			int r= *(res.begin());
			fout << "Case #"<<N<<": "<< r <<endl;
			cout << "Case #"<<N<<": "<<  r <<endl;
		} else {
			
			fout << "Case #"<<N<<": "<< "Bad magician!"<<endl;
			cout << "Case #"<<N<<": "<<  "Bad magician!"<<endl;
		}


	}

	return 0;
}