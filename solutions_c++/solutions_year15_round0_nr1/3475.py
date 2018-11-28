#include <cstdlib>
#include <cstdio>
#include <iostream>

using namespace std;

int main(){
	int csmax;
	cin >> csmax;
	for (int csnum = 1; csnum <= csmax; csnum++){
		int mshy;
		cin >> mshy;
		char shy[1002];
		cin >> shy;
		int c = 0;
		int invite = 0;
		for (int shyi = 0; shy[shyi] != '\0'; shyi++){
			int cshy = (int)(shy[shyi] - '0');
			c += cshy;
			while (c <= shyi){
				invite++;
				c++;
			}
		}
		cout << "Case #" << csnum << ": " << invite << endl;
	}
	getchar(); getchar();
	return 0;
}