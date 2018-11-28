// Lawnmower.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
using namespace std;

vector<int> getRowMinimum(vector< vector<int> > &a, int n, int m);
vector<int> getColumnMinimum(vector< vector<int> > &a, int n, int m);
vector<int> getRowMaximum(vector< vector<int> > &a, int n, int m);
vector<int> getColumnMaximum(vector< vector<int> > &a, int n, int m);
bool test(vector< vector<int> > &lawn, int n, int m);
int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("d:\\B-large.in");
	ofstream out("d:\\B-large.out");
	int number_of_test_cases = 0;

	if(!in) {
		return 0;
	}
	//收集input文件中的数据
	in >> number_of_test_cases;
	for(int k=0;k<number_of_test_cases;k++) {
		int n=0, m=0;
		in >> n;
		in >> m;

		//读入草坪样式（矩阵）数据
		vector< vector<int> > lawn(n, vector<int>(m));
		for(int i=0; i<n; ++i) {
			for(int j=0; j<m; ++j) {
				in >> lawn[i][j];
			}
		}

		//判断草坪样式是否能实现
		if(test(lawn, n, m)) {
			out<< "Case #" << k+1 << ": " << "YES" << endl;
		} else {
			out<< "Case #" << k+1 << ": " << "NO" << endl;
		}
	}

	return 0;
}

//a是n行m列的二维数组
vector<int> getRowMinimum(vector< vector<int> > &a, int n, int m) {
	vector<int> row_min(n); //每行的最小数
	for(int i=0; i<n; ++i) {
		int min = a[i][0];
		for(int j=1; j<m; ++j) {
			if(min > a[i][j]) {
				min = a[i][j];
			}
		}
		row_min[i] = min;
	}
	return row_min;
}

vector<int> getColumnMinimum(vector< vector<int> > &a, int n, int m) {
	vector<int> col_min(m); //每列的最小数
	for(int i=0; i<m; ++i) {
		int min = a[0][i];
		for(int j=1; j<n; ++j) {
			if(min > a[j][i]) {
				min = a[j][i];
			}
		}
		col_min[i] = min;
	}
	return col_min;
}

vector<int> getRowMaximum(vector< vector<int> > &a, int n, int m) {
	vector<int> row_max(n); //每行的最大数
	for(int i=0; i<n; ++i) {
		int max = a[i][0];
		for(int j=1; j<m; ++j) {
			if(max < a[i][j]) {
				max = a[i][j];
			}
		}
		row_max[i] = max;
	}
	return row_max;
}

vector<int> getColumnMaximum(vector< vector<int> > &a, int n, int m) {
	vector<int> col_max(m); //每列的最大数
	for(int i=0; i<m; ++i) {
		int max = a[0][i];
		for(int j=1; j<n; ++j) {
			if(max < a[j][i]) {
				max = a[j][i];
			}
		}
		col_max[i] = max;
	}
	return col_max;
}

bool test(vector< vector<int> > &lawn, int n, int m) {
	//vector<int> row_min = getRowMinimum(lawn, n, m);
	//vector<int> col_min = getColumnMinimum(lawn, n, m);
	vector<int> row_max = getRowMaximum(lawn, n, m);
	vector<int> col_max = getColumnMaximum(lawn, n, m);
	for(int i=0; i<n; ++i) {
		for(int j=0; j<m; ++j) {
			//当前这块草坪所处的行和列不能都有比它高的草坪，否则这种草坪的pattern就无法实现
			if(lawn[i][j] < row_max[i] && lawn[i][j] < col_max[j]) {
				return false;
			}
		}
	}
	return true;
}