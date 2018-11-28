#include<iostream>
#include<fstream>
#include<string>
using namespace std;


ifstream inFile("B-large.in");
ofstream outFile("output.txt");

string str;
int size_;
int Mat[105] = { 0 };
int Answer = 0;
int count_;

void input() {
	inFile >> str;
	
	count_ = 0;

	size_ = str.size();
	for (int i = 0; i < size_; i++)
		if (str[i] == '-')
			Mat[i] = -1;
		else
			Mat[i] = 1;

}

bool AllOK() {
	for (int i = 0; i < size_; i++)
		if (Mat[i] != 1)
			return false;
	return true;
}

void swapi() {
	int l = 0;
	int r = size_ - 1;

	while (l <= r)
	{
		int temp = -Mat[l];
		Mat[l] = -Mat[r];
		Mat[r] = temp;
		l++;
		r--;
	}
}

void swapN(int n)
{
	for (int i = 0; i <= n; i++)
		Mat[i] *= -1;
}



void proccess() {
	
	if (AllOK())
	{
		Answer = 0;
		return;
	}

	int r = size_ -1;
	while (r >= 0)
	{
		if (Mat[r] != 1)
		{
			swapN(r);
			count_++;
		}
		r--;
	}

	Answer = count_;
}


void output() {
	outFile << Answer << '\n';
}


int main() {

	while (!inFile.eof()) {
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