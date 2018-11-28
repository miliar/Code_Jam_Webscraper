#include<iostream>
#include<fstream>
#include<cstdio>
#include<string>
using namespace std;
int T;
int N;
string S;
bool F;
bool solve(int ans){
	string S1 = S;
	int Num[1001];
	for (int i = 0; i < S1.length(); i++)Num[i] = S1[i] - '0';
	Num[0] += ans;
	bool F = true;
	int stand = Num[0];
	for (int i = 1; i < S1.length(); i++){
		if (stand < i)F = false;
		stand += Num[i];
	}
	return F;
}
int main()
{
	ifstream fin("C:/Users/Toshifumi/A-large.in");
	ofstream fout("C:/Users/Toshifumi/out.txt");
	fin >> T;
	for (int i = 0; i < T; i++){
		fin >> N >> S;
		int ans = 0;
		while (true){
			if (solve(ans))break;
			ans++;
		}
		fout << "Case #" << i+1 << ": " << ans << "\n";
	}
	return 0;
}