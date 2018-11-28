#include<iostream>
#include<fstream>
#include<string>
#include <cstdlib>

using namespace std;

int main(int argc, char * argv[]){

fstream in_file;
in_file.open(argv[1], ios::in);

fstream out_file;
out_file.open("StandingOvationBig.out", ios::out);


int i;

in_file >> i;

for (int k=0; k<i; k++){
	
	int sum = 0;
	int add = 0;
	int max_shyness;
	string num_of_people;
  
	in_file >> max_shyness;
	in_file >> num_of_people;

	for (int j=0; j<max_shyness+1; j++){

		int tmp = num_of_people[j]-'0';
		while (sum < j) {
			add++;
		        sum++;	
		}  
		sum += tmp;
	}
	out_file << "Case #" << k+1 << ": " << add << endl;
}

in_file.close();
out_file.close();

return 0;
}
