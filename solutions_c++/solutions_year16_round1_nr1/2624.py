#include <iostream>
#include <string>

using namespace std;

int main()
{
	int T;
	string S;
	string R;

	cin >> T;

	for(int i=0; i<T; i++)
	{
		cin >> S;
		R = S[0];

		for(int j=1; j<S.length(); j++)
		{
			if(S[j] < R[0])
			{
				R = R+S[j];
			}
			else
			{
				R = S[j]+R;
			}
		}

		cout << "Case #" << i+1 << ": " << R << endl;
	}

	return 0;
}
