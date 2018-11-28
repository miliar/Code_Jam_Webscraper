#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int main(){

	int T, S,index,count,invites;
	string str;
	ofstream fout("Small Output.txt");
	//ifstream fin("Input.txt");
	ifstream fin("small.in");
	fin >> T;

	for (int i = 0; i < T; i++){
		fin >> S;
		fin >> str;

		index = str.at(0) - 48;
		count = index;
		invites = 0;
		for (int j = 1; j <= S; j++){
			index = str.at(j) - 48;

			if (count < j && index>0){
				invites += j - count;
				count += invites;
			}

			
			count += index;
		}
		fout << "Case #" << i + 1 << ": " << invites << endl;
	}
	system("pause");
	return 0;
}