#include <iostream>
#include <fstream>
using namespace std;

int *flag;

bool judge(int N)
{
	int temp = 0;
	int number = N;
	int sum = 0;
	while (N > 0)
	{
		temp = N % 10;
		flag[temp] = 1;
		N = N / 10;
		sum = 0;
		for (int i = 0; i < 10; i++)
		{
			sum += flag[i];
		}
		if (sum == 10)
			return true;
	}
	return false;
}
int main()
{
	int T, N;
	int t = 0;
	bool temp = false;
	ofstream out;
	out.open("A-large.out", ios::out);
	ifstream in;
	in.open("A-large.in", ios::in);
	in >> T;
	flag = new int[10];

	while (T > 0)
	{
		T--;
		t++;
		in >> N;
		for (int i = 0; i < 10; i++)
		{
			flag[i] = 0;
		}
		if (N == 0)
		{
			out << "Case #" << t << ": INSOMNIA" << endl;
			continue;
		}
//		temp = judge(N);
		int j = 0;
		int nu;
		while (!temp)
		{
			j++;
			nu = j * N;
			temp = judge(nu);
			
		}
		out << "Case #" << t << ": " << nu << endl;
		temp = false;
	}
	in.close();
	out.close();
	return 0;
}