#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
using namespace std;

bool checkOrder(string str,const vector<char>& order){
	char prev = '0';
	vector<char> thisorder;
	for (auto& it : str){
		if (prev == '0'){
			prev = it;
			thisorder.push_back(it);
		}
		else if (prev != it){
			prev = it;
			thisorder.push_back(it);
		}
	}

	if (thisorder == order){
		return true;
	}
	return false;
}


int main(){

	ofstream ofile;
	ifstream ifile;

	ifile.open("A-small-attempt1.in");
	ofile.open("output.txt");

	if (ifile.is_open()){
		string line;
		getline(ifile, line);
		int casen = stoi(line);

		for (int CASE = 0; CASE < casen; CASE++){
			getline(ifile, line);
			string nstr;
			stringstream ss(line);
			ss >> nstr;
			int n = stoi(nstr);
			vector<string> strs;
			vector<char> order;
			for (int i = 0; i < n; i++){
				getline(ifile, line);
				ss.clear();
				ss.str(line);
				string s;
				ss >> s;
				strs.push_back(s);
			}

			char prev = '0';
			for (auto& it : strs[0]){
				if (prev == '0'){
					prev = it;
					order.push_back(it);
				}
				else if (prev != it){
					prev = it;
					order.push_back(it);
				}
			}
			bool failed = false;
			vector<pair<char, int>> totals;
			for (auto& it : strs){
				if (!checkOrder(it, order)){
					failed = true;
				}
			}
			string output;
			if (!failed){
				for (auto& it : strs){
					char prev = '0';
					int total = 0;
					int ns = 0;
					for (auto& sit : it){
						if (prev == '0'){
							prev = sit;
							total++;
						}
						else if (prev != sit){
							if (ns < totals.size()){
								totals[ns].second += total;
							}
							else{
								totals.push_back(make_pair(prev, total));
							}
							total = 0;
							prev = sit;
							ns++;
							total++;
						}
						else{
							total++;
						}
					}
					if (ns < totals.size()){
						totals[ns].second += total;
					}
					else{
						totals.push_back(make_pair(prev, total));
					}
				}

				vector<pair<char,int>> averages;
				for (auto& it : totals){
					averages.push_back(make_pair(it.first, (int)floor(((float)it.second / (float)strs.size()) + 0.5f)));
				}
				string averagestr = "";
				for (int i = 0; i < order.size();i++){
					averagestr += (std::string(averages[i].second,averages[i].first));
				}

				vector<int> anums;
				char prev = '0';
				int t = 0;
				for (auto& sit : averagestr){
					if (prev == '0'){
						prev = sit;
						t++;
					}
					else if (prev != sit){
						anums.push_back(t);
						prev = sit;
						t = 1;
					}
					else{
						t++;
					}
				}
				anums.push_back(t);
				

				int moves = 0;
				for (auto& it : strs){
					vector<int> counts;
					char prev = '0';
					t = 0;
					for (auto& sit : it){
						if (prev == '0'){
							prev = sit;
							t++;
						}
						else if (prev != sit){
							counts.push_back(t);
							prev = sit;
							t = 1;
						}
						else{
							t++;
						}
					}
					counts.push_back(t);

					for (int i = 0; i < counts.size(); i++){
						moves += abs(counts[i] - anums[i]);
					}
				}
				output = to_string(moves);

			}
			else{
				output = "Fegla Won";
			}
			ofile << "Case #" << to_string(CASE + 1) << ": " << output << endl;
		}
	}

	ofile.close();
}