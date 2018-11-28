#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#define forl(i, b, e) for(int i = b; i < e; i++)
#define forlinv(i, e, b) for(int i = e; i > b; i--)

using namespace std;

int t, n;
string s;

int sumAll(int& idx, int tot){ // iniitial idx == 1 
	if (tot == 0)
		return 0;
	int ret = 0;
	forl(i, 0, tot){
		if (idx > n)
			return -1;
		ret += s[idx++] - 48;

	}
	return ret;
}

int needsFriend(){
	int idx = 1;
	int numFriend = 0; 
	int tot = s[0] - 48 ;
	while (idx <= n){
		tot = sumAll(idx, tot);
		if (tot == -1) return numFriend;
		if (tot == 0){
			numFriend++;
			tot++;
		}
	}
	return numFriend;
}


int main(void){
	fstream fin, fout;
	fin.open("D:/A-large.in", fstream::in);
	fout.open("D:/output2.txt", fstream::out);

	fin >> t;
	int tc = 0;
	while (t--){
		tc++;
		fin >> n;
		fin >> s;
		fout << "Case #" << tc << ": " << needsFriend() << endl;
		
	}
	return 0;
}