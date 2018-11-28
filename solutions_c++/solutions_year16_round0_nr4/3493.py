
#include <iostream>
#include <string>

using namespace std;
int main()
{

	
	int T;

	cin >> T;

	for(int t = 1; t <= T; t++)
	{
		int K;
		int C;
		int S;
		cin >> K;
		cin >> C;
		cin >> S;
		cout << "Case #" << t << ":";
		for(int i = 0; i < K; i++)
		{
			cout<<" "<<i+1;
		}
		cout<<endl;
	}
	
	
	
	return 0;
}
