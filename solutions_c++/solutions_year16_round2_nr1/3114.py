#include<stdio.h>
#include<vector>
#include<string>
#include<stdlib.h>
#include<algorithm>
using namespace std;

vector<int> count_arr;



int main(void){
		

	FILE *pFile = fopen("A-large.txt", "r");
	FILE *oFile = fopen("A-large_out.txt", "w");
	int testcase;

	fscanf(pFile, "%d", &testcase);

	

	for (int temp = 1; temp <= testcase; temp++){

		vector<int> result;

		//for (int k = 0; k < count_arr.size(); k++){
		//	if (count_arr[k] > 0){
		//		printf("%d번째 %c %d개 남아있음\n", temp, 'A' + k, count_arr[k]);
		//	}
		//}

		count_arr.clear();
		count_arr.resize(26, 0);

		char input_str[2222];

		fscanf(pFile, "%s", input_str);

		string input = input_str;

		for (int i = 0; i < input.size(); i++){
			count_arr[input[i] - 'A']++;
		}

		fprintf(oFile, "Case #%d: ", temp);


		while (true){

			if (min(min(count_arr['Z' - 'A'], count_arr['E' - 'A']), min(count_arr['R' - 'A'], count_arr['O' - 'A'])) == 0){
				break;
			}

			int count = min(min(count_arr['Z' - 'A'], count_arr['E' - 'A']), min(count_arr['R' - 'A'], count_arr['O' - 'A']));

			count_arr['Z' - 'A'] -= count;
			count_arr['E' - 'A'] -= count;
			count_arr['R' - 'A'] -= count;
			count_arr['O' - 'A'] -= count;

			for (int i = 0; i < count; i++){
				result.push_back(0);
			}
		}

		while (true){

			if (min(min(count_arr['S' - 'A'], count_arr['I' - 'A']), count_arr['X' - 'A']) == 0){
				break;
			}

			int count = min(min(count_arr['S' - 'A'], count_arr['I' - 'A']), count_arr['X' - 'A']);

			count_arr['S' - 'A'] -= count;
			count_arr['I' - 'A'] -= count;
			count_arr['X' - 'A'] -= count;

			for (int i = 0; i < count; i++){
				result.push_back(6);
			}
		}

		while (true){

			if (min(min(count_arr['T' - 'A'], count_arr['W' - 'A']), count_arr['O' - 'A']) == 0){
				break;
			}

			int count = min(min(count_arr['T' - 'A'], count_arr['W' - 'A']), count_arr['O' - 'A']);

			count_arr['T' - 'A'] -= count;
			count_arr['W' - 'A'] -= count;
			count_arr['O' - 'A'] -= count;

			for (int i = 0; i < count; i++){
				result.push_back(2);
			}
		}

		while (true){

			if (min(min(count_arr['F' - 'A'], count_arr['O' - 'A']), min(count_arr['U' - 'A'], count_arr['R' - 'A'])) == 0){
				break;
			}

			int count = min(min(count_arr['F' - 'A'], count_arr['O' - 'A']), min(count_arr['U' - 'A'], count_arr['R' - 'A']));

			count_arr['F' - 'A'] -= count;
			count_arr['O' - 'A'] -= count;
			count_arr['U' - 'A'] -= count;
			count_arr['R' - 'A'] -= count;

			for (int i = 0; i < count; i++){
				result.push_back(4);
			}
		}


		while (true){

			if (min(min(count_arr['F' - 'A'], count_arr['I' - 'A']), min(count_arr['V' - 'A'], count_arr['E' - 'A'])) == 0){
				break;
			}

			int count = min(min(count_arr['F' - 'A'], count_arr['I' - 'A']), min(count_arr['V' - 'A'], count_arr['E' - 'A']));

			count_arr['F' - 'A'] -= count;
			count_arr['I' - 'A'] -= count;
			count_arr['V' - 'A'] -= count;
			count_arr['E' - 'A'] -= count;

			for (int i = 0; i < count; i++){
				result.push_back(5);
			}
		}


		while (true){

			if (min(min(min(count_arr['E' - 'A'], count_arr['I' - 'A']), min(count_arr['G' - 'A'], count_arr['H' - 'A'])), count_arr['T' - 'A']) == 0){
				break;
			}

			int count = min(min(min(count_arr['E' - 'A'], count_arr['I' - 'A']), min(count_arr['G' - 'A'], count_arr['H' - 'A'])), count_arr['T' - 'A']);

			count_arr['E' - 'A'] -= count;
			count_arr['I' - 'A'] -= count;
			count_arr['G' - 'A'] -= count;
			count_arr['H' - 'A'] -= count;
			count_arr['T' - 'A'] -= count;

			for (int i = 0; i < count; i++){
				result.push_back(8);
			}
		}


		while (true){

			if (min(min(count_arr['N' - 'A'], count_arr['I' - 'A']), count_arr['E' - 'A']) == 0 || count_arr['N' - 'A'] == 1){
				break;
			}

			int count = min(min(count_arr['N' - 'A'], count_arr['I' - 'A']), count_arr['E' - 'A']);

			int Ncount = count_arr['N' - 'A'] / 2;

			if (count <= Ncount){

				count_arr['N' - 'A'] -= count * 2;
				count_arr['I' - 'A'] -= count;
				count_arr['E' - 'A'] -= count;

				for (int i = 0; i < count; i++){
					result.push_back(9);
				}
			}
			else{

				count_arr['N' - 'A'] -= Ncount * 2;
				count_arr['I' - 'A'] -= Ncount;
				count_arr['E' - 'A'] -= Ncount;

				for (int i = 0; i < Ncount; i++){
					result.push_back(9);
				}
			}
		}

		while (true){

			if (min(min(count_arr['S' - 'A'], count_arr['E' - 'A']), min(count_arr['V' - 'A'], count_arr['N' - 'A'])) == 0 || count_arr['E' - 'A'] == 1){
				break;
			}

			int count = min(min(count_arr['S' - 'A'], count_arr['E' - 'A']), min(count_arr['V' - 'A'], count_arr['N' - 'A']));

			int Ecount = count_arr['E' - 'A'] / 2;

			if (count <= Ecount){

				count_arr['S' - 'A'] -= count;
				count_arr['E' - 'A'] -= count * 2;
				count_arr['V' - 'A'] -= count;
				count_arr['N' - 'A'] -= count;

				for (int i = 0; i < count; i++){
					result.push_back(7);
				}
			}
			else{

				count_arr['S' - 'A'] -= Ecount;
				count_arr['E' - 'A'] -= Ecount * 2;
				count_arr['V' - 'A'] -= Ecount;
				count_arr['N' - 'A'] -= Ecount;

				for (int i = 0; i < Ecount; i++){
					result.push_back(7);
				}
			}
		}

		while (true){

			if (min(min(count_arr['T' - 'A'], count_arr['H' - 'A']), min(count_arr['R' - 'A'], count_arr['E' - 'A'])) == 0 || count_arr['E' - 'A'] == 1){
				break;
			}

			int count = min(min(count_arr['T' - 'A'], count_arr['H' - 'A']), min(count_arr['R' - 'A'], count_arr['E' - 'A']));

			int Ecount = count_arr['E' - 'A'] / 2;

			if (count <= Ecount){

				count_arr['T' - 'A'] -= count;
				count_arr['H' - 'A'] -= count;
				count_arr['R' - 'A'] -= count;
				count_arr['E' - 'A'] -= count * 2;

				for (int i = 0; i < count; i++){
					result.push_back(3);
				}
			}
			else{

				count_arr['T' - 'A'] -= Ecount;
				count_arr['H' - 'A'] -= Ecount;
				count_arr['R' - 'A'] -= Ecount;
				count_arr['E' - 'A'] -= Ecount * 2;

				for (int i = 0; i < Ecount; i++){
					result.push_back(3);
				}
			}
		}



		while (true){

			if (min(min(count_arr['O' - 'A'], count_arr['N' - 'A']), count_arr['E' - 'A']) == 0){
				break;
			}

			int count = min(min(count_arr['O' - 'A'], count_arr['N' - 'A']), count_arr['E' - 'A']);

			count_arr['O' - 'A'] -= count;
			count_arr['N' - 'A'] -= count;
			count_arr['E' - 'A'] -= count;

			for (int i = 0; i < count; i++){
				result.push_back(1);
			}
		}


		sort(result.begin(), result.end());

		for (int i = 0; i < result.size(); i++){
			fprintf(oFile, "%d", result[i]);
		}
		fprintf(oFile, "\n");
	}



	return 0;
}
