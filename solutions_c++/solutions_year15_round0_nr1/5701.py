#include<fstream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
void main(){
	ifstream input("A-large.in");
	ofstream output("output.txt");
	int cases;
	input >> cases;
	for (int i = 0; i != cases; ++i){
		int len,ans=0,sum=0;
		input >> len;
		string t;
		input >> t;
		vector<int> x;
		for (int j = 0; j != t.size(); ++j)
			x.push_back(stoi(t.substr(j, 1)));
		for (int j = 0; j != x.size(); ++j){
			if (x[j] != 0){
				if (sum < j){
					ans += (j - sum);
					sum += (j - sum);
				}
				sum += x[j];
			}
		}
		output << "Case #"+to_string(i+1)+": "+to_string(ans) << endl;
	}
}