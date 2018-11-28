#include<iostream>
#include<fstream>
using namespace std;

int main() {
	ifstream infile;
	infile.open("check.in");
	ofstream outfile;
	outfile.open("out.txt");
	int number_of_tests;
	infile>>number_of_tests;
	for(int case_number=1;case_number<=number_of_tests;case_number++) {
		int max_shyness;
		string shyness_count;
		infile>>max_shyness>>shyness_count;
		int answer=0;
		int number_of_people_standing=shyness_count[0]-'0';
		int i=1;
		for(;i<=max_shyness;i++) {
			if(number_of_people_standing>=i)
				number_of_people_standing=number_of_people_standing+shyness_count[i]-'0';
			else {
				int temp=i-number_of_people_standing;
				answer=answer+temp;
				number_of_people_standing=number_of_people_standing+temp+shyness_count[i]-'0';
			}
		}
		outfile<<"Case #"<<case_number<<": "<<answer<<"\n";
	}
	return 0;
}
