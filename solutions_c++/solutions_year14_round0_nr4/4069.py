#include <iostream>
#include <vector>
#include <iomanip>
#include <cstdlib>
#include <algorithm>

using namespace std;

unsigned int k;

int optimal_war_strategy (vector<double> v1, vector<double> v2){
	vector<double> ken_blocks(v1);
	vector<double> naomi_blocks(v2);

	int ken_count = 0, naomi_count = 0;
	double naomi_b;

	unsigned int index = naomi_blocks.size();

	for (unsigned int i = 0; i < index; i++){
		naomi_b = naomi_blocks[0];

		for (unsigned int j = 0; j < ken_blocks.size(); j++){

			if (ken_blocks[j] > naomi_b){
				ken_blocks.erase(ken_blocks.begin() + j);

				ken_count++;
				break;
			}

			else if(naomi_b > ken_blocks[j] && j == ken_blocks.size() - 1){
				ken_blocks.erase(ken_blocks.begin());

				naomi_count++;
			}
		}

		naomi_blocks.erase(naomi_blocks.begin());
	}

	return naomi_count;

}

/***************************************************************************************/

int optimal_deceitful_war_strategy (vector<double> ken_blocks, vector<double> naomi_blocks){
	int ken_count = 0, naomi_count = 0;
	unsigned int index = naomi_blocks.size();

	unsigned int temp;

	for (unsigned int i = 0; i < index; i++){
		temp = naomi_blocks.size() - 1;

		if (naomi_blocks[temp] > ken_blocks[temp]){
			naomi_blocks.erase(naomi_blocks.begin() + temp);
			ken_blocks.erase(ken_blocks.begin() + temp);

			naomi_count++;
		}

		else {
			naomi_blocks.erase(naomi_blocks.begin());
			ken_blocks.erase(ken_blocks.begin() + temp);

			ken_count++;
		}
	}

	return naomi_count;
}


/***************************************************************************************/

int main (){
	double temp;
	int i, testcases, size, count = 1;

	cin >> testcases;

	for (int index = 0; index < testcases; index++){
		vector<double> ken_blocks;
		vector<double> naomi_blocks;

		cin >> size;

		for (i = 1; i <= size*2; i++){
			cin >> temp;

			if (i <= size)
				naomi_blocks.push_back(temp);
			else
				ken_blocks.push_back(temp);
		}

		sort (naomi_blocks.begin(), naomi_blocks.end());
		sort (ken_blocks.begin(), ken_blocks.end());


		int first = optimal_war_strategy (ken_blocks, naomi_blocks);
		int second = optimal_deceitful_war_strategy (ken_blocks, naomi_blocks);

		cout << "Case #" << count << ": " << second << " " << first << endl;

		count++;
	}

}