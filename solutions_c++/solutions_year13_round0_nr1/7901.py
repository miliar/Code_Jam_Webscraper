#include <iostream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

string line_is_good(vector<string> cur_row) {
	//cout << "check line is good" << endl;
	//for (int j=0; j<cur_row.size(); j++) {
	//	cout << cur_row[j] << " ";
	//}
	//cout << endl;

	for (int j=0; j<cur_row.size(); j++) {
		if (cur_row[j].compare(".")==0) {
			return "bad";
		}
	}

	string first_not_T_string;
	for (int j=0; j<cur_row.size(); j++) {
		if (cur_row[j].compare("T")!=0 ) {
			first_not_T_string = cur_row[j];
		}
	}
	for (int j=0; j<cur_row.size(); j++) {
		if (cur_row[j].compare("T")==0) {
		}
		else {
			if (first_not_T_string.compare(cur_row[j])!=0) {
				return "bad";
			}
		}
	}
	return first_not_T_string;
}

void handleCase(vector<string> cur_case, int case_id) {
	vector< vector<string> > matrix;
	for (int i=0; i<cur_case.size()-1; i++) {
		vector<string> row;
		string cur_row = cur_case[i];
		//cout << "cur_row: " << cur_row << endl;
		for (int j=0; j<cur_row.size(); j++) {
			//cout << cur_row[j] << endl;
			row.push_back(cur_row.substr(j,1));
		}
		matrix.push_back(row);
	}

	//check horizontal
	//cout << "check horizontal ------------------" << endl;
	for (int i=0; i<matrix.size(); i++) {
		vector<string> cur_row = matrix[i];
		string r = line_is_good(cur_row);
		if (r.compare("bad")!=0) {
			cout << "Case #" << case_id << ": " << r << " won" << endl;
			return;
		}
	}
	//check vertical
	//cout << "check vertical ------------------" << endl;
	for (int i=0; i<matrix.size(); i++) {
		vector<string> cur_vector;
		for (int j=0; j<matrix.size(); j++) {
			vector<string> cur_row = matrix[j];
			cur_vector.push_back(cur_row[i]);
		}
		string r = line_is_good(cur_vector);
		if (r.compare("bad")!=0) {
			cout << "Case #" << case_id << ": " << r << " won" << endl;
			return;
		}
	}

	//check diagonal
	//cout << "check diagonal ------------------" << endl;
	vector<string> diag;
	for (int i=0; i<matrix.size(); i++) {
		diag.push_back(matrix[i][i]);
	}
	string r = line_is_good(diag);
	if (r.compare("bad")!=0) {
		cout << "Case #" << case_id << ": " << r << " won" << endl;
		return;
	}

	//check reverse diagonal
	//cout << "check reverse diagonal ------------------" << endl;
	vector<string> rev_diag;
	for (int i=0; i<matrix.size(); i++) {
		rev_diag.push_back(matrix[i][matrix.size()-1-i]);
	}
	r = line_is_good(rev_diag);
	if (r.compare("bad")!=0) {
		cout << "Case #" << case_id << ": " << r << " won" << endl;
		return;
	}

	//if all places are marked, then it is a draw
	//if some places are still open, then it is not finished
	for (int i=0; i<matrix.size(); i++){
		vector<string> cur_row = matrix[i];
		for (int j=0; j<cur_row.size(); j++) {
			if (cur_row[j].compare(".")==0) {
				cout << "Case #" << case_id << ": " << "Game has not completed" << endl;
				return;
			}
		}
	}
	cout << "Case #" << case_id << ": " << "Draw" << endl;

}

int main(){

	string line;
	int line_num = 0;
	int case_num = -1;
	int case_id = 0;
	int line_num_of_cur_case = 0;
	while (getline(cin,line)) {
		//cout << line << endl;
		if (line_num == 0) {
			stringstream ss;
			ss << line;
			ss >> case_num;
			//cout << "total case num: " << case_num << endl;
			line_num ++;
		}
		else {
			line_num_of_cur_case ++;
			vector<string> cur_case;
			cur_case.push_back(line);
			while (getline(cin, line)) {
				cur_case.push_back(line);
				line_num_of_cur_case ++;
				if (line_num_of_cur_case == 5) {
					line_num_of_cur_case = 0;
					case_id ++;
					handleCase(cur_case, case_id);
					cur_case.clear();
					//cout << "case_id: " << case_id << "/ case_num: " << case_num << endl;
				}
			}
			if (case_id == case_num) {
				break;
			}
		}
	}

	return 0;
}
