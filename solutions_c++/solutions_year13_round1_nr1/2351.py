#include <iostream>

using namespace std;

int main()
{
	int casettl;
	int r, t, count;
	cin >> casettl;
	for(int casenum=1; casenum<=casettl; casenum++)
	{
		cin >> r >> t;
		count=1;
		t-=2*r+1;
		for(int i=2*r+5; t>=i; i+=4)
		{
			count++;
			t-=i;
		}
		cout << "Case #" << casenum << ": " << count << endl;
	}
	return 0;
}