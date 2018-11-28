#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

bool sort2Dmat(const vector<int>& v1,const vector<int>& v2){
	return v1[1] < v2[1];
}

int main(){
	vector<vector<int> > matrix;
	int n,m;
	cin >> n >> m;
	int val;
	for(int i=0;i<n;i++){
		vector<int> vec1;
		for(int j=0;j<m;j++){
			cin >> val;
			vec1.push_back(val);
		}
		matrix.push_back(vec1);
	}

	for(int i=0;i<matrix.size();i++){
		for(int j=0;j<matrix[i].size();j++){
			cout << matrix[i][j] << "  ";
		}
		cout << endl;
	}

	vector< vector<int> >::iterator it;

	for(it=matrix.begin();it!=matrix.end();it++)
	{
		sort((*it).begin(),(*it).end());
	}
	sort(matrix.begin(),matrix.end());
	
	for(int i=0;i<matrix.size();i++){
		for(int j=0;j<matrix[i].size();j++){
			cout << matrix[i][j] << "  ";
		}
		cout << endl;
	}

	return 0;
}