#include <cstdio>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

string num[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

int main()
{
	FILE *finput = freopen("input.txt", "r", stdin);
	FILE *foutput = freopen("output.txt", "w+", stdout);

	int t_case;

	cin >> t_case;

	for(int i=1;i<=t_case;i++){
		string input;
		int input_length;
		int ans_length = 0;
		int num_cnt[30];
		vector<int> ans_set;

		for(int j=0;j<30;j++){
			num_cnt[j] = 0;
		}

		cin >> input;
		
		input_length = input.length();

		for(int j=0;j<input_length;j++){
			num_cnt[input[j] - 'A']++;
		}

		while(input_length != ans_length){
			if(num_cnt[25] > 0){
				//ZERO
				num_cnt[25]--;
				num_cnt[4]--;
				num_cnt[17]--;
				num_cnt[14]--;

				ans_length += 4;
				ans_set.push_back(0);
				continue;
			}
			
			if(num_cnt[22] > 0 ){
				//TWO
				num_cnt[19]--;
				num_cnt[22]--;
				num_cnt[14]--;

				ans_length += 3;
				ans_set.push_back(2);
				continue;
			}
			
			if(num_cnt[23] > 0){
				//SIX
				num_cnt[18]--;
				num_cnt[8]--;
				num_cnt[23]--;

				ans_length += 3;
				ans_set.push_back(6);
				continue;
			}

			if(num_cnt[5] > 0 && num_cnt[14] > 0 && num_cnt[20] > 0 && num_cnt[17] > 0){
				//FOUR
				num_cnt[5]--;
				num_cnt[14]--;
				num_cnt[20]--;
				num_cnt[17]--;

				ans_length += 4;
				ans_set.push_back(4);
				continue;
			}

			if(num_cnt[5] > 0 && num_cnt[4] > 0 && num_cnt[8] > 0 && num_cnt[21] > 0){
				//FIVE
				num_cnt[5]--;
				num_cnt[8]--;
				num_cnt[21]--;
				num_cnt[4]--;

				ans_length += 4;
				ans_set.push_back(5);
				continue;
			}

			if(num_cnt[4] > 0 && num_cnt[6] > 0 && num_cnt[8] > 0 && num_cnt[7] > 0 && num_cnt[19] > 0){
				//EIGHT
				num_cnt[4]--;
				num_cnt[8]--;
				num_cnt[6]--;
				num_cnt[7]--;
				num_cnt[19]--;

				ans_length += 5;
				ans_set.push_back(8);
				continue;
			}

			if(num_cnt[13] > 1 && num_cnt[8] > 0 && num_cnt[4] > 0){
				//NINE
				num_cnt[13] -= 2;
				num_cnt[8]--;
				num_cnt[4]--;

				ans_length += 4;
				ans_set.push_back(9);
				continue;
			}

			if(num_cnt[18] > 0 && num_cnt[4] > 1 && num_cnt[21] > 0){
				//SEVEN
				num_cnt[18]--;
				num_cnt[4] -= 2;
				num_cnt[21]--;
				num_cnt[13]--;

				ans_length += 5;
				ans_set.push_back(7);
				continue;
			}

			if(num_cnt[4] > 1 && num_cnt[19] > 0 && num_cnt[17] > 0 && num_cnt[7] > 0){
				//THREE
				num_cnt[19]--;
				num_cnt[7]--;
				num_cnt[17]--;
				num_cnt[4] -= 2;

				ans_length += 5;
				ans_set.push_back(3);
				continue;
			}

			if(num_cnt[14] > 0 && num_cnt[13] > 0){
				//ONE
				num_cnt[14]--;
				num_cnt[13]--;
				num_cnt[4]--;

				ans_length += 3;
				ans_set.push_back(1);
				continue;
			}
		}

		sort(ans_set.begin(),ans_set.end());

		cout << "Case #" << i <<": ";
		for(int j=0;j<ans_set.size();j++){
			cout << ans_set[j];
		}
		cout << endl;
	}


	return 0;
}