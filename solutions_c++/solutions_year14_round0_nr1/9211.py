#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string.h>

using namespace std;

string data[] = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"};

int main(){
	ifstream input("A-small-attempt2.in");
	ofstream out("out");
	int x;
	input >> x;
	for(int t = 1;  t <= x;  t++){
		int row = 0, valor = 0, result = -1;
		bool dp[17];
		memset(dp, false, sizeof(dp));
		input >> row;
		for(int i = 1; i <= 4;  i++){
			for(int j = 1; j <= 4; j++){
				input >> valor;
				if(i == row){
					dp[valor] = true;
				}
			}
		}
		input >> row;
		for(int i = 1; i <= 4;  i++){
			for(int j = 1; j <= 4; j++){
				input >> valor;
				if(i == row && dp[valor]){
					result = result == -1 ? valor : result * 0;
				}
			}
		}				
		string str = "Volunteer cheated!";
		if(result == 0)
			str = "Bad magician!";
		else if(result != -1)
			str = data[result];
		out << "Case #" << t <<": " << str <<endl;
		if(input.eof()) break;
	}
	input.close();
	out.close();	
	return 0;
}

