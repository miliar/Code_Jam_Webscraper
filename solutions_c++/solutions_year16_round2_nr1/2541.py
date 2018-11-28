#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
#include <stdlib.h>


using namespace std;

bool find_delete_char(string &s, char c){
	int pos = s.find_first_of(c);
	if(pos != string::npos){
		s = s.substr(0, pos) + s.substr(pos+1, -1);
		return true;
	}
	else{
		return false;
	}
}

string find_answer(string sinput){
	vector<int> a;
	string s=sinput;
	while (s.size() > 0){
		//0
		if (find_delete_char(s,'Z')){
			find_delete_char(s, 'E');
			find_delete_char(s, 'R');
			find_delete_char(s, 'O');
			a.push_back(0);
		}
		//2
		else if (find_delete_char(s,'W')){
			find_delete_char(s, 'T');
			find_delete_char(s, 'O');
			a.push_back(2);
		}
		//6
		else if (find_delete_char(s,'X')){
			find_delete_char(s, 'I');
			find_delete_char(s, 'S');
			a.push_back(6);
		}
		//8
		else if (find_delete_char(s,'G')){
			find_delete_char(s, 'E');
			find_delete_char(s, 'I');
			find_delete_char(s, 'H');
			find_delete_char(s, 'T');
			a.push_back(8);
		}
		//3
		else if (find_delete_char(s,'T')){
			find_delete_char(s, 'E');
			find_delete_char(s, 'R');
			find_delete_char(s, 'H');
			find_delete_char(s, 'E');
			a.push_back(3);
		}
		//7
		else if (find_delete_char(s,'S')){
			find_delete_char(s, 'E');
			find_delete_char(s, 'V');
			find_delete_char(s, 'E');
			find_delete_char(s, 'N');
			a.push_back(7);
		}
		//5
		else if (find_delete_char(s,'V')){
			find_delete_char(s, 'F');
			find_delete_char(s, 'I');
			find_delete_char(s, 'E');
			a.push_back(5);
		}
		//4
		else if (find_delete_char(s,'F')){
			find_delete_char(s, 'O');
			find_delete_char(s, 'U');
			find_delete_char(s, 'R');
			a.push_back(4);
		}
		//1
		else if (find_delete_char(s,'O')){
			find_delete_char(s, 'E');
			find_delete_char(s, 'N');
			a.push_back(1);
		}
		//9
		else if (find_delete_char(s,'N')){
			find_delete_char(s, 'I');
			find_delete_char(s, 'N');
			find_delete_char(s, 'E');
			a.push_back(9);
		}
		
	}
	sort(a.begin(),a.end());
	string answer="";
	for (int i =0; i < a.size(); i++){
		answer+= to_string(a[i]);
	}
	return answer;
}

int main(int argc, char *argv[]) {
	int n;
	ifstream infile("A-large.in");
	ofstream outfile("p1largeout.txt");

	infile >> n;
	for (int i = 0; i < n; i++){
		string s;
		infile >> s;
		outfile << "Case #"<< i+1 << ": "<< find_answer(s) << endl;
	}	
	
	infile.close();
	outfile.close();
}