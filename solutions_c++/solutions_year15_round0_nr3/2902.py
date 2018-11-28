#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int arr[5][5] = { {0, 0, 0, 0,0},{0, 1, 2, 3, 4 }, {0, 2, -1, 4, -3 }, {0, 3, -4, -1, 2 }, {0, 4, 3, -2, -1 } };

int giveIndex(char c)
{
	if (c == '1')
		return 1;
	else if (c == 'i')
		return 2;
	else if (c == 'j')
		return 3;
	else if (c == 'k')
		return 4;
}

int main(){

	int T,index,total,j;
	long long int X,L;
	string temp,str;
	ifstream fin("C-small-attempt1.in");
	ofstream fout("output.txt");
	fin >> T;

	for (int i = 0; i < T; i++){
		fin >> L;
		fin >> X;
		fin >> temp;
		str = "\0";
		for (int j = 0; j < X; j++)
			str.append(temp);
				
		total = giveIndex(str.at(0));
		for (j = 1; total!=2 && j < str.length(); j++){

			index = giveIndex(str.at(j));
						
			if (total < 0){
				total = -1 * total;
				total = arr[total][index];
				total = -1 * total;
			}
			else
				total = arr[total][index];
		}
		if (j == str.length()){
			fout << "Case #" << i + 1 << ": NO" << endl;
			continue;
		}
		
		total = giveIndex(str.at(j));
		for (j = j + 1; total != 3 && j < str.length(); j++){

			index = giveIndex(str.at(j));

			if (total < 0){
				total = -1 * total;
				total = arr[total][index];
				total = -1 * total;
			}
			else
				total = arr[total][index];
		}

		if (j == str.length()){
			fout << "Case #" << i + 1 << ": NO" << endl;
			continue;
		}
		total = giveIndex(str.at(j));
		for (j = j + 1; j < str.length(); j++){

			index = giveIndex(str.at(j));

			if (total < 0){
				total = -1 * total;
				total = arr[total][index];
				total = -1 * total;
			}
			else
				total = arr[total][index];
		}

		if (total==4)
			fout << "Case #" << i + 1 << ": YES" << endl;
		else
			fout << "Case #" << i + 1 << ": NO" << endl;

	}
	return 0;
}