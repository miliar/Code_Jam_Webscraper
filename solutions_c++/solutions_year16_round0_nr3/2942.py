#include<iostream>
#include<string>
#include<math.h>
#include<fstream>
using namespace std;
int N = 16;
int J = 50;

string output[300];

void prepros()
{
	
	for (int i = 1; i < J+3; i++)
	{
		output[i] = "";
		output[i] += '1';
		for (int j = 1; j < N-1; j++)
		{
			output[i] += '0';
		}
		output[i] += '1';
		int temp = i;
		int cnt = 0;
		while (temp)
		{
			output[i][cnt + 1] = (temp % 2) + '0';
			
			cnt++;
			temp /= 2;
		}int k = 0;
		for (int j = 0; j < cnt; j++)
		{
			output[i][N - cnt + j-1] = output[i][j];
		}
	}
}
int main()
{
	ofstream cout("output.txt");
	int T1,T2,T3;
	//cin >> T1 >> T2 >> T3;
	cout << "Case #1:" << endl;
	prepros();
	for (int i = 1; i <= J; i++)
	{
		cout << output[i];
		
		for (int k = 2; k <= 10; k++)
		{
			int div = 0;
			for (int digit = 0; digit < 9; digit++)
			{
				div += pow(k, digit)*((int)output[i][N-1-digit] - '0');
			}
			cout << " " << div;
		}
		cout << endl;

	}
	return 0;
}