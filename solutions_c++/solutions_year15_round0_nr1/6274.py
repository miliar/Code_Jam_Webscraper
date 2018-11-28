#include <iostream>
#include <sstream>

using namespace std;

int main() {
	int N,Smax, sum, count;
	string S;
	stringstream ss;
	ss.str("");
	S.reserve(1002);	

	cin >> N;

	for (int i = 0; i < N; i++)
	{
		cin >> Smax >> S;
		sum = 0;
		count = 0;
		for (int j = 0; j < S.length(); j++)
			if (sum > Smax)
				break;
			else if (j < sum)
				sum+= S[j] - '0';
			else
			{
				count += (j - sum);
				sum+= j - sum + S[j] -'0';				
			}
			
		ss << "Case #" << i+1 << ": " << count << endl;
	}
	
	cout <<	ss.str();
}


