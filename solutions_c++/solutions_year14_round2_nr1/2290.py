#include<iostream>
#include<string>
#include<fstream>
using namespace std;
#include<string.h>

int main(void) {
	int T,N;
	int count[2][110];
	string s[100];
	ifstream cin("A-small-attempt3.in");
	ofstream cout("A.out");
	cin >> T;
	for(int i = 0; i < T; i++){
		cin >> N;
		for(int j = 0; j < N; j++)
			for(int k = 0; k < 110; k++)count[j][k] = 0;
		cout << "Case #"<<i+1<<": ";
		for(int j = 0; j < N; j++)cin >> s[j];
		string tmp0 = "";char tmpc = '0';
		int index = 0;
		for(int j = 0; j < s[0].size();j++){
			if(tmpc!=s[0][j]){tmp0+=s[0][j];tmpc=s[0][j];index++;}
			else count[0][index]++;
		}
		string tmp1 = "";tmpc = '0';
		index = 0;
		for(int j = 0; j < s[1].size();j++){
			if(tmpc!=s[1][j]){tmp1+=s[1][j];tmpc=s[1][j];index++;}
			else count[1][index]++;
		}
		if(tmp0.compare(tmp1))cout << "Fegla Won"<<endl;
		else {
			int move = 0;
			for(int j = 1;j <= tmp0.size(); j++){
				move+=count[0][j]>count[1][j]?count[0][j]-count[1][j]:count[1][j]-count[0][j];
			}
			cout << move << endl;
		}
	}
	system("pause");
    return 0;
}