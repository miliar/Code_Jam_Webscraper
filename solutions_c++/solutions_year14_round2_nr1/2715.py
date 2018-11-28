
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>



using namespace std;



int main() {
	fstream fin("A-small-attempt2.in");
//	fstream fin("in.txt");
	fstream fout("out.txt");

	int n, N, ans;


	fin >> n;

	for(int i = 0; i < n; i++){
		ans = -2;
		fin >> N;
		vector<char> mas[N];
		string str;


		for (int j = 0; j < N; j++){
			fin >> str;
			for(int k = 0; k < str.size(); k++){
				mas[j].push_back(str[k]);
			}

		}

		vector<pair<char, int> > priority[N];
		pair<char, int> temp;
		for (int j = 0; j < N; j++){
			temp.first = mas[j][0];
			temp.second = 1;
			priority[j].push_back(temp);
			for(int k = 0; k < mas[j].size(); k++){
				if(priority[j].back().first != mas[j][k]){
					temp.first = mas[j][k];
					priority[j].push_back(temp);
				} else {
					priority[j][priority[j].size() - 1].second++;
				}
			}
			//kastil
			priority[j][0].second--;
			/*for(long k = 0; k < priority[j].size(); k++){
				fout << priority[j][k].first << " _ " << priority[j][k].second << endl;
			}
			fout  << endl;*/
		}

		for (int j = 0; j < N-1; j++){////////////////////////
			if(priority[j].size() != priority[j+1].size()){
				ans = -1;
			}
		}

		if(ans == -1){
			fout << "Case #" << i+1 << ": " << "Fegla Won" << endl;
			continue;
		}/////////////////////

		for (int j = 0; j < N-1; j++){//////////////////////////////////
			for(int k = 0; k < priority[j].size(); k++){
				if(priority[j][k].first != priority[j+1][k].first){
					ans = -1;
				}
			}
		}
		if(ans == -1){
					fout << "Case #" << i+1 << ": " << "Fegla Won" << endl;
					continue;
		}/////////////////////////////////
		ans = 0;
		double mid[priority[0].size()];

		for(int k = 0; k < priority[0].size(); k++){
			mid[k] = 0;
			for (int j = 0; j < N; j++){
					mid[k] += priority[j][k].second;
			}
			//fout << "!!! " << mid[k] << " !!!" << endl;
			mid[k] /= N;

			if ((int)mid[k] + 0.5 < mid[k]){
				mid[k] = (int)mid[k]+1;
			} else {
				mid[k] = (int)mid[k];
			}

			for (int j = 0; j < N; j++){
				if (priority[j][k].second - mid[k] >= 0)
					ans += priority[j][k].second - (int)mid[k];
				else
					ans -= priority[j][k].second - (int)mid[k];
			}
		}



		fout << "Case #" << i+1 << ": " << ans << endl;

	}

	fin.close();
	fout.close();
	return 0;
}
