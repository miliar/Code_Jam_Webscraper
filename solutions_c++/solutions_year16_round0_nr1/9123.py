#include <iostream>
#include <vector>
using namespace std;

typedef vector<bool> VB;

VB seen;
int c, N, k;

bool verify()
{
	for(int i = 0; i < 10; ++i)
	{
		if(!seen[i]) return false;
	}
	return true;
}

void evaluate(int i)
{
	k = i*N;
	if(k == 2*k)
	{
		cout << "Case #" << c << ": INSOMNIA" << endl; 
		return;
	}
	
	int m = k;
	while(m > 0)
	{
		int dig = m%10;
		seen[dig] = true;
		m = m/10;
	}
	if(verify()) 
	{
		cout << "Case #" << c << ": " << k << endl;
		return;
	}
	
	evaluate(i + 1);
}

int main()
{
	int total;
	cin >> total;
	for(c = 1; c <= total; ++c)
	{
		cin >> N;
		seen = VB(10,false);
		k = N;
		evaluate(1);
	}
}
