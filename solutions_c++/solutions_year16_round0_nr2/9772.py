#include<iostream>
#include<fstream>
using namespace std;

#define Max_S 110
#define STOP {cin.sync();cin.get();}

ifstream fin("input.txt");
ofstream fout("output.txt");

void reverse(char *ch, int num){
	char temp;

	for (int i = 0; i <= num / 2; i++){
		temp = ch[i];

		if (ch[num - i] == '+')
			ch[i] = '-';
		else
			ch[i] = '+';

		if (temp == '+')
			ch[num - i] = '-';
		else
			ch[num - i] = '+';
	}
}

void solve(int num){
	char ch[Max_S];

	//cin >> ch;
	fin >> ch;

	int top;
	int bottom = strlen(ch) - 1;
	//first and last '-'

	int count = 0;

	for (top = 0; ch[top] == '+'; top++);
	for (; bottom != top&&ch[bottom] == '+'; bottom--);

	while (bottom != -1){

		if (top != 0)
			reverse(ch, top - 1);
		else
			reverse(ch, bottom);

		for (top = 0; ch[top] == '+'; top++);
		for (; bottom != top&&ch[bottom] == '+'; bottom--);

		count++;
	}

	//cout << "Case #" << num << ": " << count << endl;
	fout << "Case #" << num << ": " << count << endl;
}

int main(){
	int T;
	//cin >> T;
	fin >> T;

	for (int num = 1; num <= T; num++){
		solve(num);
	}

	//STOP;
	return 0;
}