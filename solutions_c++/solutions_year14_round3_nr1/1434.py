#include <iostream>
#include <string>
#include <sstream>

using namespace std;

long long stringToInt(string s)
{
	istringstream iss(s);
	long long n;
	iss >> n;
	return n;
}

int main()
{
	int T;
	cin >> T;
	cin.ignore();
	for (int t = 1; t <= T; ++t)
	{
		long long P,Q;
		string S;
		getline(cin,S,'/');
		P = stringToInt(S);
		getline(cin,S);
		Q = stringToInt(S);
		double R = (P*1.0)/(Q*1.0), R1 = R;

		int count = 0, count1 = 0;


		bool flag = false;
		while(count < 41)
		{
			R *= 2.0;
			count++;
			if(R - 1 == 1 || R - 1 == 0)
			{
				flag = true;
				break;
			}
			if(R > 1)
			{
				R -= 1;
			}
		}

		while(R1 < 1 && count1 < 41)
		{
			R1 *= 2.0;
			++count1;
		}
		
		cout << "Case #" << t << ": "; 

		if(count > 40 || count > 41)
			cout << "impossible\n";
		else
			cout << count1 << "\n";
	}
	return 0;
}