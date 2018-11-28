#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
using namespace std;

bool checkRow(vector<string> v, char c){
	for (int i = 0; i < 4; i++){
		bool is = true;
		for (int j = 0; j < 4; j++)
			if (v[i][j] != c && v[i][j] != 'T')
				is = false;
		if (is) 
			return true;
	}
	return false;
}

bool checkColumn(vector<string> v, char c){
	for (int i = 0; i < 4; i++){
		bool is = true;
		for (int j = 0; j < 4; j++)
			if (v[j][i] != c && v[j][i] != 'T')
				is = false;
		if (is) 
			return true;
	}
	return false;
}

bool checkDiag(vector<string> v, char c){
	bool is1 = true;
	for (int i = 0; i < 4; i++){
		if (v[i][i] != c && v[i][i] != 'T')
				is1 = false;
	}
	bool is2 = true;
	for (int i = 0; i < 4; i++){
		if (v[i][3 - i] != c && v[i][3 - i] != 'T')
				is2 = false;
	}
	return is1 || is2;
}

bool check(vector<string> v, char c){
	if (checkRow(v, c))
		return true;
	if (checkColumn(v, c))
		return true;
	if (checkDiag(v, c))
		return true;
	return false;
}

bool draw(vector<string> v){
	for (int i = 0; i < 4; i++){
		for (int j = 0; j < 4; j++)
			if (v[i][j] == '.')
				return false;
	}
	return true;
}

int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int T;
	cin>>T;

	for (int t = 0; t < T; t++){
		vector<string> v;

		for (int i = 0; i < 4; i++){
			string s;
			cin>>s;
			v.push_back(s);
		}

		cout<<"Case #"<<t + 1<<": ";

		if (check(v, 'X'))
			cout<<"X won";
		else if (check(v, 'O'))
			cout<<"O won";
		else if (draw(v))
			cout<<"Draw";
		else 
			cout<<"Game has not completed";
		
		cout<<endl;;
	}
}
