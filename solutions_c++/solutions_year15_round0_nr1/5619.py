#include<iostream>
#include<fstream>

using namespace std;

int main(){

	char line[1010];	//Smax=6 +2 =8
	int total_test_cases = 0;
	int total_standing_people = 0;
	int total_levels=0;
	int current_standing_people = 0;
	int answer=0;
	char ch[1];
	

	ifstream ifile; ofstream ofile;
	ifile.open("A-large.in");
	ofile.open("output2.out");
	ifile.getline(line, 1010);			//Smax=6
	total_test_cases = atoi(line);

		for (int case_no = 1; case_no <= total_test_cases; case_no++){
			answer = 0; total_standing_people = 0; total_levels = 0; current_standing_people = 0; answer = 0;
			ifile.getline(line, 1010);		//Smax=6
			total_levels = atoi(line);

		//while (line[0]!=' '){
		//	for (int index = 0; line[index] != '\0'; index++){
		//		line[index] = line[index + 1];
		//	}
		//}
		//for (int index = 0; line[index] != '\0'; index++){
		//	line[index] = line[index + 1];
		//}

			int increment = 0;
			while (line[increment] != ' '){
				increment++;
			}
			increment++;

		for (int level = 0; level <=total_levels; level++){
			ch[0] = line[level+increment];	//0-9
			current_standing_people = atoi(ch);

			if (level == 0){
				total_standing_people += current_standing_people;
			}
			else {
				while (total_standing_people < level){
					total_standing_people++;
					answer++;
				}
				total_standing_people += current_standing_people;
			}
		}
		ofile << "Case #" << case_no << ": " << answer<<endl;
	}
	return 0;
}