#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef unsigned int ui;

struct Senator{
	ui count;
	char name;
};

bool sortByCount(const Senator &lhs, const Senator &rhs){
	return (lhs.count > rhs.count);
}

int main(){

	ui T = 0;
	cin >> T;
	ui caseNumber = 1;
	ui num_party = 0;
	ui alphabet = (int)'A';
	ui temp = 0;
	ui total_sum = 0;

	while(T--){
		cin >> num_party;
		vector<Senator> s(num_party);
		alphabet = 'A';
		total_sum = 0;

		for(int index=0; index<num_party; index++){
			cin >> s[index].count;			
			s[index].name = (char)(alphabet + index);
			total_sum += s[index].count;
		}

		sort(s.begin(),s.end(),sortByCount);

		cout << "Case #" << caseNumber << ":";

		while(total_sum > 3){

			if(s[0].count != 0){
				cout << " " << s[0].name;
				s[0].count--;
				total_sum--;
			}

			if(s[1].count != 0){
				cout << s[1].name;
				s[1].count--;
				total_sum--;
			}
			if(num_party > 2){
				sort(s.begin(),s.end(),sortByCount);	
			}
		}

		if(total_sum == 2){
			cout << " " << s[0].name;
			cout << s[1].name;
		}
		else{
			cout << " " << s[0].name;
			s[0].count--;
			sort(s.begin(),s.end(),sortByCount);
			cout << " " << s[0].name;
			cout << s[1].name;	
		}

		cout << endl;

		caseNumber++;
	}

	return 0;
}