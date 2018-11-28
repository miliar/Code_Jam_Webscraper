#include <iostream>
using namespace std;

int main()
{
	int tt;
	cin >> tt;
	for(int t = 0; t < tt; t++)
	{
		int K,C,S;
		cin >> K >> C >> S;
		cout << "Case #" << t+1 << ":";
		for(int i=0;i<S;i++)
		{			
			cout << " " << i + 1 ;
		}
		cout << endl;
	}
	return 0;
}