#include <iostream>
#include <vector>
#include <stdlib.h>     /* atoi */
using namespace std;

int main() {
	// your code goes here
	int trials;
	cin >> trials;
	for (int i = 0 ; i < trials ; i++ ){
		int answer1;
		string line;
		string temp;
		vector<int> nums;
		cin >> answer1;
		if (answer1 == 1){
			getline(std::cin, temp);
			
			getline(std::cin, line);			
			getline(std::cin, temp);
			getline(std::cin, temp);
			getline(std::cin, temp);
			//cout << "line 1";
		}
		else if (answer1 == 2){
			getline(std::cin, temp);
			
			getline(std::cin, temp);
			getline(std::cin, line);
			getline(std::cin, temp);
			getline(std::cin, temp);
			//cout << "line 2" << endl;
		}
		else if (answer1 == 3){
			getline(std::cin, temp);
			
			getline(std::cin, temp);
			getline(std::cin, temp);
			getline(std::cin, line);
			getline(std::cin, temp);
			//cout << "line 3" << endl;
		}
		else {
			getline(std::cin, temp);
			
			getline(std::cin, temp);
			getline(std::cin, temp);
			getline(std::cin, temp);
			getline(std::cin, line);
			//cout << "line 4" << endl;
		}
		//cout << line << endl;
		string temp2;
		for (int j = 0 ; j < line.length() ; j++)
		{
			if (line[j]==' '){
				nums.push_back(atoi(temp2.c_str()));
				temp2 = "";
			}
			else if ( j == (line.length()-1) ){
				temp2 += line[j];				
				nums.push_back(atoi(temp2.c_str()));
				temp2 = "";
			}
			else {
				temp2 += line[j];
			}
			
		}
		int answer2;
		string line2;
		string temp3;
		//vector<int> nums;
		cin >> answer2;
		if (answer2 == 1){
			getline(std::cin, temp3);
			
			getline(std::cin, line2);			
			getline(std::cin, temp3);
			getline(std::cin, temp3);
			getline(std::cin, temp3);
			//cout << "line 1";
		}
		else if (answer2 == 2){
			getline(std::cin, temp3);
			
			getline(std::cin, temp3);
			getline(std::cin, line2);
			getline(std::cin, temp3);
			getline(std::cin, temp3);
			//cout << "line 2" << endl;
		}
		else if (answer2 == 3){
			getline(std::cin, temp3);
			
			getline(std::cin, temp3);
			getline(std::cin, temp3);
			getline(std::cin, line2);
			getline(std::cin, temp3);
			//cout << "line 3" << endl;
		}
		else {
			getline(std::cin, temp3);
			
			getline(std::cin, temp3);
			getline(std::cin, temp3);
			getline(std::cin, temp3);
			getline(std::cin, line2);
			//cout << "line 4" << endl;
		}
		//cout << line2 << endl;
		string temp4;
		int count = 0;
		int ans;
		for (int j = 0 ; j < line2.length() ; j++)
		{
			if (line2[j]==' '){
				int t = atoi(temp4.c_str());
				//cout << t << endl;
				for (int k = 0 ; k<nums.size();k++){
					if (t == nums[k]){
						count++;
						ans = t;
					}
				}
				//nums.push_back(atoi(temp2.c_str()));
				temp4 = "";
			}
			else if ( j == (line2.length()-1) ){
				temp4 += line2[j];				
				int t = atoi(temp4.c_str());
				for (int k = 0 ; k<nums.size();k++){
					if (t == nums[k]){
						count++;
						ans = t;
					}
				}
				//nums.push_back(atoi(temp2.c_str()));
				temp4 = "";
			}
			else {
				temp4 += line2[j];
			}
			
		}
		cout << "Case #"<<i+1<< ": ";
		if (count == 1){
			cout << ans << endl;
		}
		else if (count > 1){
			cout << "Bad magician!" << endl;			
		}
		else {
			cout << "Volunteer cheated!" << endl;			
		}
		//for (int j = 0 ; j < nums.size(); j++){
		//	cout << nums[j] << " ";
		//}
		
	}
	return 0;
}