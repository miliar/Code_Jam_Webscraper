#include <iostream>

using namespace std;

int main(void)
{
	int T, iT;
	string S;

	cin >> T;

	iT = 0;
	while(iT++ < T)
	{
		int nums[10] = {0};
		char alph['Z' + 1] = {0};

		cout << "Case #" << iT << ": ";
		cin >> S;

		for(int i = 0; i < S.size(); i++)
		{
			alph[ S[i] ]++;	
		}

		// Remove first uniques = 0, 2, 4, 6, 8
		while(alph['Z']) nums[0]++, alph['Z']--,alph['E']--,alph['R']--,alph['O']--; 
		while(alph['W']) nums[2]++, alph['T']--,alph['W']--,alph['O']--; 
		while(alph['U']) nums[4]++, alph['F']--,alph['O']--,alph['U']--,alph['R']--; 
		while(alph['X']) nums[6]++, alph['S']--,alph['I']--,alph['X']--; 
		while(alph['G']) nums[8]++, alph['E']--,alph['I']--,alph['G']--,alph['H']--,alph['T']--;

		// Remove second uniques = 1, 3, 5, 7, 9
		while(alph['O']) nums[1]++, alph['O']--,alph['N']--,alph['E']--; 
		while(alph['T']) nums[3]++, alph['T']--,alph['H']--,alph['R']--,alph['E']--,alph['E']--; 
		while(alph['F']) nums[5]++, alph['F']--,alph['I']--,alph['V']--,alph['E']--; 
		while(alph['S']) nums[7]++, alph['S']--,alph['E']--,alph['V']--,alph['E']--,alph['N']--;
		while(alph['N']) nums[9]++, alph['N']--,alph['I']--,alph['N']--,alph['E']--; 
		

		for(int i = 0; i < 10; i++)
		{	
			while(nums[i]) cout << i, nums[i]--;
		}

		cout << endl;
	}

	return 0;
}