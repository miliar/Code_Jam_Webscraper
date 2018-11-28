#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;


string vecstr(vector<int> vec) {
	std::stringstream buf;
	buf <<"[";
	for (int i =0; i < vec.size(); i++) {
		buf << vec[i];
		buf << ",";
	}
	buf <<"]";
	return buf.str();
	
}

string vecbool(vector<bool> vec) {
	std::stringstream buf;
	buf <<"[";
	for (int i =0; i < vec.size(); i++) {
		buf << vec[i];
		buf << ",";
	}
	buf <<"]";
	return buf.str();
	
}

int find_index(vector<int> vec, int val) {
	for (int i =0 ; i < vec.size(); i++) {
		if (vec[i] == val)
			return i;
	}
}


vector<bool> check_even(vector<int> row) {
	int max_val = *max_element(row.begin(), row.end());
	int max_pos = find_index(row, max_val);
	vector<bool> result;
	int high = row[0];
	int low = row[0];
	bool prev = true;
	for (int i=0; i < row.size(); i++) {
		if (row[i] < max_val) {
			result.push_back(false);
		} else {
			result.push_back(true);
		}
		/*
		if (row[i] < high) {
			prev = false;
			result.push_back(false);
		} else {
			int high = row[i];
			result.push_back(true);
		}
		*/
		//result.push_back(prev);
	}
	//cout << "Even" << endl;
	//cout << vecstr(row) << endl;
	//cout << vecbool(result) << endl;
	return result;
}

vector<bool> check_odd(vector<int> row) {
	vector<bool> result;
	int max_val = *max_element(row.begin(), row.end());
	int max_pos = find_index(row, max_val);
	int high = row[row.size() - 1];
	bool prev = true;
	for (int i= row.size() - 1 ; i >= 0 ; i--) {
		if (row[i] < max_val) {
			result.push_back(false);
		} else {
			result.push_back(true);
		}
		/*
		if (row[i] < high) {
			prev = false;
			result.push_back(false);
		} else {
			int high = row[i];
			result.push_back(true);
		}
		*/
		//result.push_back(prev);
	}
	reverse(result.begin(),result.end());
	//cout << "ODD" << endl;
	//cout << vecstr(row) << endl;
	//cout << vecbool(result) << endl;
	return result;
}



bool check_grid(vector< vector<int> > grid, int oddeven =0 ) {
	vector< vector <bool > > row_results;
	vector< vector <bool > > col_results;
 	for (int i =0; i < grid.size(); i ++) {
		if (i % 2 == oddeven) {
			row_results.push_back(check_even(grid[i]));
		} else {
			row_results.push_back(check_odd(grid[i]));
		}
	}
 	
 	vector< vector<int> > cgrid(grid[0].size(), vector<int>(grid.size()));
	for (int i =0; i < grid.size(); i ++) {
		for (int j=0; j < grid[i].size(); j++) {
			cgrid[j][i]  = grid[i][j];
		}
	}
 
	for (int i =0; i < cgrid.size(); i ++) {
		if (i % 2 == oddeven) {
			col_results.push_back(check_even(cgrid[i]));
		} else {
			col_results.push_back(check_odd(cgrid[i]));
		}
	}

 	
	if (col_results.size() == 0) {
		for (int i =0; i < row_results.size(); i++) {
			for (int j =0; j < row_results[i].size(); j++) {
				if (row_results[i][j] == false)
					return false;
			}
		}
	} else {
		
		//cout << "ROWS: " << row_results.size() << " COLS: " << col_results.size() << endl;
		for (int i =0; i < row_results.size(); i++) {
			//cout << vecbool(row_results[i]) << endl;
			for (int j =0; j < row_results[i].size(); j++) {
				//cout << "in row: " << row_results[i].size() << " COLS: " << col_results[j].size() << endl;
				//cout << "TESTING " << i << " " << j << endl;
				
				row_results[i][j] = row_results[i][j]  || col_results[j][i];
				if (row_results[i][j] == false) {
					return false;
				}
				//cout << "FINISH TESTING " << i << " " << j << endl;
			}
			
			//cout << vecbool(row_results[i]) << endl;
			//cout << endl;
			
		}
	}
	return true;
}



bool check_case(vector< vector<int> > grid) {
	
	
	
	//return check_grid(grid, 0);
	/*
	for (int i=0; i < grid.size(); i++) {
	
			cout << vecstr(grid[i]) << endl;
	}
	*/
	//cout << "CHECKEs: " <<  check_grid(grid, 0) << " " << check_grid(grid, 1) << endl;
	return check_grid(grid, 0) and check_grid(grid, 1);
	if (check_grid(grid, 0) ==true)
		return true;
	else
		return check_grid(grid, 1);
		
}
string result(bool out) {
	if (out == true)
		return "YES";
	return "NO";
}
int main(int argc, char *argv[]) {
	string line;
	int N;
	getline(cin, line);
	stringstream nstream(line);
	nstream >> N;
	for (int i =0; i < N; i ++) {
		int n, m;
		getline(cin, line);
		stringstream nmstream(line);
		nmstream >> n;
		nmstream >> m;
		vector< vector<int> > grid;
		for (int j = 0; j < n; j++ ) {
			vector<int> row;
			getline(cin, line);
			stringstream stream(line);
			for (int k =0; k < m; k++) {
				int tmp;
				stream >> tmp;
				row.push_back(tmp);
			}
			grid.push_back(row);
		}
		cout << "Case #"<< (i+1) << ": " << result(check_case(grid)) << endl;
	}
}
