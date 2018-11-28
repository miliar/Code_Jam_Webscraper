
#include <iostream>
#include <string>

using namespace std;


int main()
{
	int T;

	cin >> T;

	for(int t = 1; t <= T; t++)
	{
		string S;
		cin >> S;
		string result;
		
		for(int i = 0; i<S.length();i++)
		{
			if(i == 0)
				result.insert(result.begin(),1,S[i]);
			else if(S[i]>=result[0])
				result.insert(result.begin(),1,S[i]);
			else 
				result.insert(result.end(),1,S[i]);


		}
		cout << "Case #" << t << ": ";
		cout <<result <<endl;
		
	}
	

	return 0;
}


