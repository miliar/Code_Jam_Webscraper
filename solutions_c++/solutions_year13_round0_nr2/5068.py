#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>

using namespace std;
bool checkH(const vector<vector<int> > &arry, vector<vector<bool> > &isValid, int row,int num) {
	int j = 0;
	for (j = 0; j < arry[0].size(); ++j) {
		if (isValid[row][j] || arry[row][j] == num) continue;
		break;
	}
	return j== arry[0].size()? true: false;
}


bool checkV(const vector<vector<int> > &arry, vector<vector<bool> > &isValid, int col, int num) {
	int i = 0;
	for (i = 0; i < arry.size(); ++i) {
		if (isValid[i][col] || arry[i][col] == num) continue;
		break;
	}
	return i== arry.size()? true: false;

}
void markH(vector<vector<bool> > &isValid, int row){
	for (int j =0; j <isValid[0].size(); ++j) {
		isValid[row][j] = true;
	}
}
void markV(vector<vector<bool> > &isValid, int col) {
	for (int i =0; i < isValid.size(); ++i) {
		isValid[i][col] = true;
	}
}



bool checkNum(const vector<vector<int> > &arry, vector<vector<bool> > &isValid, int num) {
	for (int i =0; i < arry.size(); ++i) {
		for (int j = 0; j < arry[0].size(); ++j) {
			if (isValid[i][j]) continue;
			if (arry[i][j] != num) continue;
			bool ch = checkH(arry, isValid, i, num);
			bool cv = checkV(arry, isValid, j, num);
			if (ch) {
				markH(isValid, i);
			} 
			if (cv) {
				markV(isValid, j);
			} 

			if (ch ==0 && cv == 0)
				return false;
		}
	}
	return true;
}



int main() {
	fstream in, out;
	in.open("proba.in", fstream::in);
	out.open("proba.out", fstream::out);

	int line_no;
	in >> line_no;
	for (int l = 1; l <=line_no; ++l) {
		int m, n;
		in >> m, in >> n;
		vector<vector<int> > arr(m, vector<int>(n, 0));
		set<int> si;
		for (int i=0; i < m; ++i) {
			for (int j = 0; j < n; ++j) {
				in>> arr[i][j];
				si.insert(arr[i][j]);
			}
		}
		if (m == 1 || n == 1) {
			out << "Case #" << l << ": YES" << endl;
			continue;
		}

		vector<vector<bool> > isValid(m, vector<bool>(n, false));
		bool res = true;
		for(set<int>::iterator it = si.begin(); it != si.end(); ++it) {
			if (!checkNum(arr, isValid, *it)) {
				res = false;
				break;
			}
		}

		string result = res?"YES":"NO";
		out << "Case #" << l << ": " << result.c_str() <<  endl;
	}

	in.close();
	out.close();
	return 0;

}