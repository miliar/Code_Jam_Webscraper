#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>

typedef long long ll;

using namespace std;


int get_minus_segments_after(string &st, int indx){
	int cnt = 0;
	
	for(int i = indx + 1; i < st.size(); i++){
		if(st[i] == '-' && st[i-1] == '+') cnt++;	
	}

	return cnt;
}

int index_of(string &st, char ch){
	for(int i = 0; i < st.size(); i++)
		if(st[i] == ch) return i;

	return -1;
}

int main(){
	
	ifstream fin;
	ofstream fout;

	fin.open("input.txt");
	fout.open("output.txt");


	
	int t;
	fin >> t;

	for(int q = 0; q < t; q++){
		string st;
		fin >> st;
		
		int ans = 0;

		if(st[0] == '-'){
			int indx = index_of(st,'+');
			if(indx == -1) ans = 1;
			else {
				int minus_segments = get_minus_segments_after(st,indx);
				ans = 2 * minus_segments + 1;
			}
		} else {
			int minus_segments = get_minus_segments_after(st,0);
			ans = 2 * minus_segments;
		}

		fout << "Case #" << q+1<< ": " << ans << endl;
	}
	return 0;
}