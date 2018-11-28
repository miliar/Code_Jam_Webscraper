#include <iostream>
#include <string>

using namespace std;

int g_mask[10];

class Solver
{
public:
	Solver() 
	{
		m_hasDigit = 0x3ff;
	}
	void getInput()
	{
		cin >> N;
	}
	void solve()
	{
		if (N == 0) {
			cout << "INSOMNIA";
			return;
		}
		int current = 0;
		while (m_hasDigit != 0) {
			current += N;
			checkDigit(current);
		}
		cout << current;
	}
	void checkDigit(int input)
	{
		while (input > 0) {
			m_hasDigit &= g_mask[input % 10];
			input /= 10;
		}
	}
	int N;
	int m_hasDigit;
};

int main()
{
	for (int i = 0; i < 10; i++) {
		g_mask[i] = 0x3ff - (1 << i);
	}
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		Solver mySolver;
		mySolver.getInput();
		cout << "Case #" << i + 1 << ": ";
		mySolver.solve();
		cout << endl;
	}
	return 0;
}