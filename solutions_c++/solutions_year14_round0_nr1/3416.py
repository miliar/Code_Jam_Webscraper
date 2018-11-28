#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <stdlib.h>
using namespace std;
string solve(vector<vector<int> > v1, int r1, vector<vector<int> > v2, int r2){
	vector<int> v=v1[r1];
	sort(v.begin(), v.end());
	vector<int> res;
	for(int i=0; i<v2[r2].size(); i++){
		int j=0;
		while(j<v.size()&&v[j]<v2[r2][i]){
			j++;
		}
		if(v2[r2][i]==v[j])	res.push_back(v[j]);
	}
	if(res.size()==1)	return to_string(res[0]);
	else if(res.size()==0)	return "Volunteer cheated!";
	else	return "Bad magician!";
}
int main(){
	ifstream ifs("test.txt");
	ofstream ofs("a-small.out");
	int t;
	ifs>>t;
	for(int i=1; i<=t; i++){
		int r1, r2;
		ifs>>r1;
		vector<vector<int> > v1;
		for(int i=0; i<4; i++){
			vector<int> row;
			for(int j=0; j<4; j++){
				int tmp;
				ifs>>tmp;
				row.push_back(tmp);
			}
			v1.push_back(row);
		}
		ifs>>r2;
		vector<vector<int> > v2;
		for(int i=0; i<4; i++){
			vector<int> row;
			for(int j=0; j<4; j++){
				int tmp;
				ifs>>tmp;
				row.push_back(tmp);
			}
			v2.push_back(row);
		}
		stringstream ss;
		ss<<"Case #"<<i<<": "<<solve(v1, r1-1, v2, r2-1)<<endl;
		cout<<ss.str();
		ofs<<ss.str();
	}
}