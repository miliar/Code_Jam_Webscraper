#include <iostream>
#include <map>
#include <string>
using namespace std;

map<string, map<string, string>> table;

string add_minus(string s){
	if (s[0] == '-')
		return string(1, s[1]);
	else
		return '-' + s;
}
string multiply(string i, string j){
	if (i[0] == '-' && j[0] == '-'){
		return table[string(1, i[1])][string(1, j[1])];
	}
	else if (i[0] == '-'){
		return add_minus(table[string(1, i[1])][j]);
	}else if (j[0] == '-'){
		return add_minus(table[i][string(1, j[1])]);
	}
	else{
		return table[i][j];
	}

}



int main(){
	int T;

	
	map<string, string> first;
	first["1"] = "1";
	first["i"] = "i";
	first["j"] = "j";
	first["k"] = "k";
	table["1"] = first;

	map<string, string> second;
	second["1"] = "i";
	second["i"] = "-1";
	second["j"] = "k";
	second["k"] = "-j";
	table["i"] = second;

	map<string, string> third;
	third["1"] = "j";
	third["i"] = "-k";
	third["j"] = "-1";
	third["k"] = "i";
	table["j"] = third;

	map<string, string> fourth;
	fourth["1"] = "k";
	fourth["i"] = "j";
	fourth["j"] = "-i";
	fourth["k"] = "-1";
	table["k"] = fourth;


	cin >> T;
	for (int t = 1; t <= T; t++){
		int L, X;
		string s;
		string temp="";
		cin >> L >> X;
		cin >> s;

		for (int i = 0; i < X; i++){
			temp += s;
		}
		s = temp;
		temp = "1";
		string next = "i";


		string g=multiply("-1", "-1");

		bool find = false;
		for (int i = 0; i < s.length(); i++){
			temp=multiply(temp, string(1,s[i]));
			if (next=="i" && temp == next){
				next = "k";
			}
			else if (next == "k" && temp == next){
				next = "-1";
			}
			else if (next == "-1" && temp==next && i == s.length() - 1){
				find = true;
			}
		}

		cout << "Case #" << t << ": ";
		if (find)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
		

	}
}