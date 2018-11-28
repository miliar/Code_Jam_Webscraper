#include <iostream>
#include <string>
#include <cstring>
#include <fstream>
#include <limits.h>
using namespace std;
//#define DEBUG
int str[1001];
int Sum[1001];
int main(){
	ifstream ifs("C:\\Users\\kawa\\Downloads\\A-large.in");
	ofstream ofs("C:\\Users\\kawa\\Downloads\\output.txt");
	int T;
#ifdef DEBUG
	cin >> T;
#else
	ifs >> T;
#endif
	for (int i = 1; i <= T; ++i){
		int MAX;
#ifdef DEBUG
		cin >> MAX;
#else
		ifs >> MAX;
#endif
		memset(str, 0, sizeof(str)); memset(Sum, 0, sizeof(Sum));
		string STR; 
#ifdef DEBUG
		cin >> STR;
#else 
		ifs >> STR;
#endif
		for (int j = 0; j <= MAX; ++j){
			char ch; ch = STR[j];
			str[j] = ch - '0';
		}
		// ‚»‚Ìshyness level ‚É“ž’B‚µ‚½‚Æ‚«‚ÌSum
		Sum[0] = str[0];
		for (int j = 1; j <= MAX; ++j){
			Sum[j] = Sum[j - 1] + str[j];
		}
		int cnt = 0; int add = 0; int crr = 0;
		for (int j = 0; j < MAX; ++j){
			if (Sum[j] + add < j + 1) add += j + 1 - (Sum[j] + add);
		}
#ifdef DEBUG
		cout << "Case #" << i << ": " << add << '\n';
#else 
		ofs << "Case #" << i << ": " << add << '\n';
#endif
	}
}