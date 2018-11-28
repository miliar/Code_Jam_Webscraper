#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

ifstream in("A-small-attempt0.in");
ofstream out("o1.txt");
int first[4];
int second[4];
void getcase(){
	int ans1;
	in >> ans1;
	int slave;
	for(int i = 0;i<16;i++){
		in >> slave;
		if(i>=4*ans1-4 && i<=4*ans1-1){
			first[i%4] = slave;
		}
	}
	int ans2;
	in >> ans2;
	for(int i = 0;i<16;i++){
		in >> slave;
		if(i>=4*ans2-4 && i<=4*ans2-1){
			second[i%4] = slave;
		}
	}
	//Result 0 means that it works, Result 1 is bad magician, Result 2 is volunteer cheated, -1 is undetermined.
	bool found = false;
	int result = -1;
	int answer = 0;
	//i is for first array, j is for second.
	for(int i = 0;i<4;i++){
		for(int j = 0;j<4;j++){
			if(first[i] == second[j]){
				if(!found){
					answer = first[i];
					found = true;
					result = 0;	
				}else{
					result = 1;
				}
			}
		}
	}
	if(!found){
		result = 2;
	}
	if(result == 0){
		out << answer;
	}else if(result == 1){
		out << "Bad magician!";
	}else if(result == 2){
		out << "Volunteer cheated!";
	}else{
		out << "UHOH ERROR.";
	}
}
int main(){
	int T;
	in >> T;
	for(int i = 1;i<=T;i++){
		out << "Case #" << i << ": ";
		getcase();
		out << "\n";
	}
	return 0;
}
