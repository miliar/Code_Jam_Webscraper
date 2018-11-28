
#include <iostream>
#include <fstream>
#include <stack>
#include <vector>
#include <stdlib.h>
using namespace std;
ifstream my("A-small-attempt0.in");
ofstream of("a.txt");
int main() {
	int all;
	int temp;
	my>>all;
	for(int a = 1; a <= all; a++){
		int answers;
		my>>answers;
		int line1[4],line2[4];
		for(int i = 1; i <= 4; i++){
			for(int j = 0; j < 4; j++){
				if(i == answers)
					my>>line1[j];
				else
					my>>temp;
			}
		}
		my>>answers;
		for(int i = 1; i <= 4; i++){
			for(int j = 0; j < 4; j++){
				if(i == answers)
					my>>line2[j];
				else
					my>>temp;
			}
		}
		int count = 0;
		int card;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				//of<<line1[i]<<" "<<line2[j]<<"\n";
				if(line1[i] == line2[j]){
					count++;
					card = line1[i];
				}
			}
		}
		of<<"Case #"<<a<<": ";
		if(count == 0){
			of<<"Volunteer cheated!"<<"\n";
		}else if(count == 1)
			of<<card<<"\n";
		else
			of<<"Bad magician!"<<"\n";
	}
	return 0;
}
