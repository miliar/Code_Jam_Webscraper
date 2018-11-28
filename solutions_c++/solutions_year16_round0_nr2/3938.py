#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	fstream fs;
  fs.open ("input.txt");

	int round_num, n;
	fs >> round_num;

	string hehe;
	getline(fs, hehe);

	for(int r = 1; r < round_num+1; r++){
		string cake;
		getline(fs, cake);
		char last = 'a';
		int count = 0;

		for (int i=0; i<cake.size(); i++){
			if (cake[i] != last){
				count++;
				last = cake[i];
			}
		}
		if (cake[cake.size()-1] == '+')
			count--;

		cout << "Case #" << r << ": " << count << endl;
	}


	fs.close();


	return 0;
}
