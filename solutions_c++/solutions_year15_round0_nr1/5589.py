#include <iostream>
using namespace std;

int main() {
	int friends, n, smax, total_ppl, curr_j;
	string in;
	cin >> n;

	
	for (int i = 0; i < n; i++)
	{
		cin >> smax >> in;
		friends = total_ppl = 0;
		
		for (int j = 0; j <= smax; j++)
		{
			curr_j = in[j] - '0';
			if (j > total_ppl && curr_j!=0) 
			{
				friends += j-total_ppl;
				total_ppl = j;
			}
			total_ppl += curr_j;
		}

		cout << "Case #" << i+1 << ": " << friends <<endl;
		
	}
	
	return 0;
}