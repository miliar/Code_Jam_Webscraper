#include<fstream>
#include<string>
#include<vector>
#include<algorithm>
#include<iostream>
using namespace std;
bool check(vector<int> &x){
	int ans = 0;
	for (auto i : x){
		if (i == 1)
			++ans;
		else if (i != 0)
			return false;
	}
	if (ans == 2)
		return true;
}
int main(){
	ifstream in("A-large.in");
	ofstream out("output.txt");
	int t;
	in >> t;
	for (int i = 1; i <= t; ++i){
		out << "Case #" << i << ": ";
		string s("ABCDEFGHIJKLMNOPQRSTUVWXYZ");
		int r, temp, sum = 0;
		in >> r;
		vector<int> x;
		for (int j = 0; j != r; ++j){
			in >> temp;
			x.push_back(temp);
		}
		for (auto i : x)
			sum += i;
		if (x.size() == 2){
			for (int i = 0; i != x[0]; ++i)
				out << "AB" << ' ';
		}
		else{
			while (!check(x)){
				int max = -1, ind;
				for (int i = 0; i != x.size(); ++i){
					if (x[i] > max){
						ind = i;
						max = x[i];
					}
				}
				if (max > sum / 2)
					cout << "err" << endl;
				sum -= 1;
				x[ind] -= 1;
				out << s[ind] << ' ';
			}
			string temp;
			for (int j = 0; j != x.size(); ++j){
				if (x[j] == 1){
					temp += s[j];
				}
			}
			out << temp;
		}
		out << endl;
	}
}
