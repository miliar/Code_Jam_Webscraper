// Magic Trick.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

using namespace std;

vector<int> intersect(int[], int[]);

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("d:\\Code jam\\Magic Trick\\A-small-attempt0.in");
	ofstream out("d:\\Code jam\\Magic Trick\\A-small-attempt0.out");
	int T = 0;
	int length = 4;
	int row_1 = -1;
	int row_2 = -1;
	int square_grid_1[4][4];
	int square_grid_2[4][4];
	vector<int> result;
	vector<int>::size_type size;


	in >> T;
	for(int t=1;t<=T;t++) {
		//读取输入参数
		in >> row_1;
		for(int i=0;i<length;i++) {
			for(int j=0;j<length;j++) {
				in >> square_grid_1[i][j];
			}
		}
		in >> row_2;
		for(int i=0;i<length;i++) {
			for(int j=0;j<length;j++) {
				in >> square_grid_2[i][j];
			}
		}

		result = intersect(square_grid_1[row_1 - 1], square_grid_2[row_2 - 1]);
		size = result.size();

		if(size < 1) {
			out << "Case #" << t << ": " << "Volunteer cheated!" << endl;
		} else if(size == 1) {
			out << "Case #" << t << ": " << result[0] << endl;
		} else if(size > 1) {
			out << "Case #" << t << ": " << "Bad magician!" << endl;
		}
	}

	return 0;
}

//取两个长度为4的数组的交集
vector<int> intersect(int a[], int b[]) {
	int length = 4;
	vector<int> intersection;
	
	for(int i=0;i<length;i++) {
		for(int j=0;j<length;j++) {
			if(a[i] == b[j]) {
				intersection.push_back(a[i]);
			}
		}
	}
	
	return intersection;
}