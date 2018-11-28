#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <stack>
#include <algorithm>
using namespace std;

template<class T>
bool pairCompare(const T & x, const T & y)
{
  return x.second < y.second;
}

template<class T>
typename T::const_iterator map_max_element(const T &A)
{
    typedef typename T::value_type pair_type;
    return max_element(A.begin(), A.end(), pairCompare<typename T::value_type>);
}

int main(int argc, const char* argv[]) { 

	int ntest = 0; 
	int nrow = 4; 
	int ncol = 4; 
	cin >> ntest; 
	int testcase = 1; 
	while (ntest--) { 
		int row1, row2; 
		vector<vector<int> > board1(4, vector<int>(4)); 
		vector<vector<int> > board2(4, vector<int>(4)); 

		cin>> row1; 
		for (int i = 0; i < nrow; i++) 
			for (int j = 0; j < ncol; j++)
				cin>> board1[i][j]; 
		cin >> row2; 
		for (int i = 0; i < nrow; i++) 
			for (int j = 0; j < ncol; j++)
				cin>> board2[i][j]; 

		std::map<int, int> map1; 
		//cout<<"row1 = " << row1<< " row2 = " << row2<< endl;
		//for (int i = 0; i < ncol; i++) { 
		//	cout << board1[row1-1][i] << " ";
		//}
		//cout << endl; 
		//for (int i = 0; i < ncol; i++) { 
		//	cout << board2[row2-1][i] << " ";
		//}
		//cout << endl; 

		for (int i = 0; i < ncol; i++) { 
			map1[board1[row1-1][i]] = 1; 
		}

		int count = 0; 
		int value; 
		for (int i = 0; i < ncol; i++) { 
			if (map1.count(board2[row2-1][i]) > 0) { 
				count++;
				value = board2[row2-1][i]; 
			}
		}
		switch (count) { 
			case 0: 
				cout << "Case #"<<testcase<<": Volunteer cheated!"<<endl; 
				break; 
			case 1:
				cout << "Case #"<<testcase<<": "<<value <<endl; 
				break; 
			default: 
				cout << "Case #"<<testcase<<": Bad magician!"<<endl; 
		}
		testcase++; 
		
	}
	return 0; 
}
