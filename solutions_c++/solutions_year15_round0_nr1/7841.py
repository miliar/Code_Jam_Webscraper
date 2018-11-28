#include <fstream>
#include <sstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<string> split(const string &str, char delim) {
		istringstream iss(str);
		string tmp;
		vector<string> res;
		while(getline(iss, tmp, delim)) {
				res.push_back(tmp);
		}
		return res;
}

string solve(int c, string str) {
	cout << "solve start c : " << c << " str : " << str << endl;
	int total_num = 0;
	int plus_num = 0;

	for(int i = 0 ; i <= c ; i++) {
			cout << "solve index : " << i << " total_num : " << total_num << endl;
			if (total_num < i) {
					plus_num += i - total_num;
					total_num = i;
			}
			cout << "solve index : " << i << " str : " << str[i] << endl;
			total_num += stoi(str.substr(i,1));
	}
	cout << "solve plus_num : " << plus_num << endl;
	return to_string(plus_num);
}


int main(int argc, char *argv[]) {

	//ファイル読み込み
	ifstream fin(argv[1]);
	
	string test_case_str;	
	getline(fin, test_case_str);
	int test_case = stoi(test_case_str);
	string buffer;
	//INPUTファイルの読み込み
	vector<vector<string> > input_list;
	for(int i = 0 ; i < test_case; i++) {
			getline(fin,buffer);
			vector<string> input = split(buffer, ' ');
			input_list.push_back(input);
	}
	fin.close();
	
	//問題を解く
	vector<string> output_list;
	for(vector<string> input : input_list) {
		output_list.push_back(solve(stoi(input[0]), input[1]));
	}
	//結果を出力する
	ofstream fout(argv[2]);	
	for(int i = 0 ; i < output_list.size() ; i++ ) {
		fout << "Case #" << i+1 << ": " << output_list[i] << endl; 
	}
	fout.close();
	return 0;
}


