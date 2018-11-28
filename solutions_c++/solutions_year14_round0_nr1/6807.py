#include <iostream>
#include <fstream>
#include <vector>
#include <array>
using namespace std;
void MagickTrick();


int main(){
	MagickTrick();

	return 0;
}

void MagickTrick(){
	fstream in;
	ofstream out;
	out.open("Text.out");
	in.open("1.txt");
	int n;
	in >> n;
	array<array<int, 4>, 4> grid;
	array<int, 4> temp;
	int answer = 0;
	int card;
	for (int i = 0; i < n; i++){
		answer = 0;
		int aim;
		in >> aim;

		for (auto& row : grid){
			for (auto& elem : row){
				in >> elem;
			}
		}

	
		std::copy(grid[aim-1].begin(), grid[aim-1].end(), temp.begin());

		in >> aim;

		for (auto& row : grid){
			for (auto& elem : row){
				in >> elem;
			}
		}

		for (auto& elem : grid[aim - 1]){
			auto res = std::find(temp.begin(), temp.end(), elem);
			if (res != temp.end()){
				if (answer == 0){
					answer = 1;
					card = elem;
				}
				else
					answer = 2;
			}
		}

		switch (answer){
		case 0:
			out << "Case #" << i + 1 << ": " << "Volunteer cheated!" << endl;
			break;
		case 1:
			out << "Case #" << i + 1 << ": " << card << endl;
			break;
		case 2:
			out << "Case #" << i + 1 << ": " << "Bad magician!" << endl;
			break;
		}
	}
}
