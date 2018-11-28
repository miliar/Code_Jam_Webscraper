#include<iostream>
#include<fstream>
using namespace std;


ifstream inFile("A-large.in");
ofstream outFile("output.txt");

int N;
int Mat[15] = { 0 };
int Answer = 0;

void input() {
	inFile >> N;

	Answer = 0;
	for (int i = 0; i < 10; i++)
		Mat[i] = 0;
}

void check(int N) {
	while (N > 0)
	{
		Mat[N % 10] = 1;
		N = N / 10;
	}
}

bool allZero() {

	for (int i = 0; i < 10; i++)
		if (Mat[i] == 0)
			return false;
	return true;
}

void proccess() {

	for (int i = 1; i  < 100 ; i++)
	{
		check(N*i);
		
		if (allZero())
		{
			Answer = N * i;
			break;
		}

	}

}

void output() {
	if (Answer == 0)
		outFile << "INSOMNIA" << '\n';
	else
		outFile << Answer << '\n';

}


int main() {

	while(!inFile.eof()){
		int T;
		inFile >> T;


		
		for (int i = 0; i < T; i++)
		{
			input();
			proccess();
			outFile << "CASE #";
			outFile << i + 1;
			outFile << ": ";
			output();
		}

		break;
	}

}