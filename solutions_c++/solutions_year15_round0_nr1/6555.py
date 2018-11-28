#include <iostream>
#include <string>
#include <algorithm>
#include <utility>

using namespace std;

int s_maxs[100];
int stats[100][1001];
int audience_no[100];
int invite_friend_no[100];

int main(){
	//input
	int test_case_no;
	cin >> test_case_no;
	string stats_buf;
	for (int i = 0; i < test_case_no; i++){
		cin >> s_maxs[i] >> stats_buf;
		audience_no[i] = 0;
		for (int j = 0; j < stats_buf.size(); j++){
			stats[i][j] = (stats_buf[j] - '0');
			audience_no[i] += stats[i][j];
		}
		//cout << stats_buf << endl;
	}

	//calculate
	int standing_audiences;
	for (int i = 0; i < test_case_no; i++){
		standing_audiences = 0;
		invite_friend_no[i] = 0;
		for (int j = 0; j < s_maxs[i] + 1; j++){
			if (standing_audiences == audience_no[i]){
				break;
			}
			if (standing_audiences >= j){
				standing_audiences += stats[i][j];
			} else {
				invite_friend_no[i] += (j - standing_audiences);
				audience_no[i] += (j - standing_audiences);
				standing_audiences += ((j - standing_audiences) + stats[i][j]);
			}
		}

	}

	//output
	for (int i = 0; i < test_case_no; i++){
		cout << "Case #" << i + 1 << ": " << invite_friend_no[i] << endl;
	}

	return 0;

}