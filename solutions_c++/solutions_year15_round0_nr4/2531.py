#include<fstream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
string solve(vector<int> v, int x){
	sort(v.rbegin(), v.rend());
	int r = v[0], c = v[1];
	if (r*c < x || (r*c%x != 0 )|| x>6 || max(r, c) < x)
		return "r";
	if (x == 1)
		return "g";
	if (x == 2){
		return (r*c % 2 == 0) ? "g" : "r";
	}
	if (x == 3){
		if (r == 4 && c == 3)
			return "g";
		if (r == 3 && c == 3)
			return "g";
		if (r == 3 && c == 2)
			return "g";
		if (r == 3 && c == 1)
			return "r";
	}
	if (x == 4){
		if (r == 4 && c == 4)
			return "g";
		if (r == 4 && c == 3)
			return "g";
		if (r == 4 && c == 2)
			return "r";
		if (r == 4 && c == 1)
			return "r";
	}
}
void main(){
	ifstream input("D-small-attempt0.in");
	ofstream output("output.txt");
	int cases,temp;
	input >> cases;
	for (int i = 0; i != cases; ++i){
		int x;
		vector<int> v;
		input >> x;
		input >> temp;
		v.push_back(temp);
		input >> temp;
		v.push_back(temp);
		output << "Case #" + to_string(i + 1) + ": ";
		output << (solve(v, x) == "g" ? "GABRIEL" : "RICHARD") << endl;
	}
}
