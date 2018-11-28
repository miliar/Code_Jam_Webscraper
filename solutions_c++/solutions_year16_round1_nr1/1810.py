#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<fstream>
#pragma warning (disable : 4996)

using namespace std;

int main() {

	ifstream read;
	read.open("A.in");
	//FILE* write = fopen("A.txt", "w");
	
	ofstream write("A.txt");

	int t;

	read >> t;

	
	for (int i = 0;i < t;i++) {

		string s;
		read >> s;

		string last;
		last = s[0];

		for (int j = 1;j < s.length();++j) {
			
			string choice1;
			choice1 = s[j];
			choice1.append(last);
			
			string choice2;
			choice2 = last + s[j];


			choice1 < choice2 ? last = choice2 : last = choice1;
		}

		

		write << "Case #"<<i+1<<": " << last<<endl;
		

	}
	
	read.close();
	write.close();

	return 0;
}