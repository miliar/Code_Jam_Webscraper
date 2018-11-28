#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

int main(){
	ifstream input;
	input.open("try.txt");
	string hold;
	getline(input,hold);
	int number = stoi(hold);
	string holderer;
	vector<string> seq;
	while(getline(input,holderer)){
		seq.push_back(holderer);
	}
	vector<int> ans;
	ofstream output;
	output.open("result1.txt");
	for (int i = 0; i < number; ++i){
		output << "Case #" << i+1 << ": ";
		//int holder = seq[i].size();
		cout << "in: "<< seq[i].size() << endl;
		size_t fnd;
		for(int k=0; k<seq[i].size(); k++){
				if(seq[i][k]=='Z'){
					ans.push_back(0);
				}
				else if(seq[i][k]=='W'){
					ans.push_back(2);
				}
				else if(seq[i][k]=='X'){
					ans.push_back(6);
				}
				else if(seq[i][k]=='G'){
					ans.push_back(8);
				}
		}
		cout << "gggg" << endl;
		for(int k=0;k<ans.size();k++){
			if(ans[k]==0){
				
				fnd = seq[i].find('Z');
				if (fnd!=std::string::npos){
					cout << "fsfasfd: " << seq[i] << endl;
					seq[i].erase(seq[i].begin()+fnd);
					cout << "fsfasfd: " << seq[i] << endl;
					fnd = 0;
				}

				fnd = seq[i].find('E');
				if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
				fnd = seq[i].find('R');
				if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
				fnd = seq[i].find('O');
				if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}

			}
			else if(ans[k]==2){
				fnd = seq[i].find('T');
				if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
				fnd = seq[i].find('W');
				if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
				fnd = seq[i].find('O');
				if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
			}
			else if(ans[k]==6){
				fnd = seq[i].find('S');
				if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
				fnd = seq[i].find('I');
				if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
				fnd = seq[i].find('X');
				if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
			}
			else if(ans[k]==8){
				fnd = seq[i].find('E');
				if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
				fnd = seq[i].find('I');
				if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
				fnd = seq[i].find('G');
				if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
				fnd = seq[i].find('H');
				if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
				fnd = seq[i].find('T');
				if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
			}
		}
			cout << "good" << endl;
			string gh = seq[i];

			for(int k=0; k<gh.size(); k++){
				if(gh[k]=='S'){
					ans.push_back(7);
					fnd = seq[i].find('S');
					if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
					fnd = seq[i].find('E');
					if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
					fnd = seq[i].find('V');
					if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
					fnd = seq[i].find('E');
					if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
					fnd = seq[i].find('N');
					if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
				}
			}
			gh = seq[i];
			for(int k=0; k<gh.size(); k++){
				if(gh[k]=='V'){
					ans.push_back(5);
					fnd = seq[i].find('F');
					if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
					fnd = seq[i].find('I');
					if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
					fnd = seq[i].find('V');
					if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
					fnd = seq[i].find('E');
					if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
				}
			}
			gh = seq[i];
			for(int k=0; k<gh.size(); k++){
				if(gh[k]=='F'){
					ans.push_back(4);
					fnd = seq[i].find('F');
					if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
					fnd = seq[i].find('O');
					if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
					fnd = seq[i].find('U');
					if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
					fnd = seq[i].find('R');
					if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
				}
			}
			gh = seq[i];
			for(int k=0; k<gh.size(); k++){
				if(gh[k]=='O'){
					ans.push_back(1);
					fnd = seq[i].find('O');
					if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
					fnd = seq[i].find('N');
					if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
					fnd = seq[i].find('E');
					if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
				}
			}
			gh = seq[i];
			for(int k=0; k<gh.size(); k++){
				if(gh[k]=='T'){
					ans.push_back(3);
					fnd = seq[i].find('T');
					if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
					fnd = seq[i].find('H');
					if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
					fnd = seq[i].find('R');
					if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
					fnd = seq[i].find('E');
					if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
					fnd = seq[i].find('E');
					if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
				}
				if(gh[k]=='I'){
					ans.push_back(9);
					fnd = seq[i].find('N');
					if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
					fnd = seq[i].find('I');
					if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
					fnd = seq[i].find('N');
					if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
					fnd = seq[i].find('E');
					if (fnd!=std::string::npos){
					seq[i].erase(seq[i].begin()+fnd);
					fnd = 0;
				}
				}	
			}
			sort(ans.begin(),ans.end());
			cout << "hii!!!  "<< seq[i].size() << endl;

			for (int k = 0; k < ans.size(); ++k)
				{
							/* code */
							output << ans[k];
				}
				output << endl;
				ans.clear();	
		
	}
}