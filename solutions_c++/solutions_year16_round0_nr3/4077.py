#include<iostream>
#include<fstream>
#include<string>
#include<cmath>
using namespace std;

char A[33] = { 0 };
int case_[12] = { 0 };

int N, J;
void input() {
	cin >> N >> J;
	A[N-1] = '1';  A[0] = '1';
}


bool isPrime(int n) {

	string str = A;
	long long temp = stoll(str,0, n);
	bool check = false;
	for (long long i = 2; i*i <= temp; i++)
	{
		if (temp % i == 0)
		{
			case_[n] = i;
			check = true;
		}
	}
	return check;
}

void swaping(int n)
{
	if (J == 0)return;
	if (n < 1 ) {

	for (int i = 2; i <= 10; i++)
		if (!isPrime(i)) {
			return;
		}


	J--;
	
	for (int i = 0; i < N; i++)
		cout << A[i];

	for (int i = 2; i <= 10; i++)
	{ 
		cout << " " << case_[i]  ;
	}
	cout << endl;


		return;
	}

	A[n] = '1';

	swaping(n - 1);
	
	A[n] = '0';
	
	swaping(n - 1);
}

void proccess() {

	int sizz = J;
	swaping(N - 2);
}

int main() {

	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		input();
		cout << "CASE #" << i + 1 << ": \n";
		proccess();

	}


}