#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(){

	int NSteps;
	cin >> NSteps;

	for(int t=1; t<=NSteps; t++){
		cout << "Case #" << t << ": ";
		int N;
		cin >> N;


		vector< vector<int> > number(N, vector<int>(110));
		vector< vector<int> > letter(N, vector<int>(110,-1));
		int MM = 1000000;
		int NN = -1;
		vector<int> min(110,MM);
		vector<int> max(110,NN);
		string s;
		for(int i=0; i<N; i++){
			cin >> s;
			char c = s.at(0);
			int pos=0;
			for(int j=0; j<s.length(); j++){
				if(c != s.at(j))
					pos++;
				c = s.at(j);
				letter[i][pos] = c-'a';
				number[i][pos]++;
			}
		}

		bool fail = false;
		for(int j=0; j<110; j++){
			for(int i=0; i<N; i++){
				if(letter[i][j] != letter[0][j]){
					fail = true;
				}
				if(number[i][j] > max[j])
					max[j] = number[i][j];
				if(number[i][j] < min[j])
					min[j] = number[i][j];
			}
		}

		for(int j=0; j<110; j++){
			for(int i=0; i<N; i++){
				if(number[i][j]==0 && max[j] != 0){
					fail=true;
				}
			}
		}


		if(fail)
			cout << "Fegla Won" << endl;
		else{
			int no = 0;
			for(int j=0; j<110; j++){
				no += max[j]-min[j];
			}
			cout << no << endl;
		}
	}
}
