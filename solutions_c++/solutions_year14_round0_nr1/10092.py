// by Neo

#include<iostream>
#include<vector>
#include<string>
#include<cmath>
#include<algorithm>
#include<set>
#include<map>
using namespace std;

#pragma warning(disable:4996)

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);

	const string BAD_MAGICIAN = "Bad magician!";
	const string VOLUNTEER_CHEATED = "Volunteer cheated!";

	int T = 0;
	cin >> T; // Read the Number of cases
	int ans1, ans2, dummy; 
	int num1[4], num2[4];

	for(int t = 0; t < T; t++) 
	{
		cin >> ans1;
		for(int i = 0; i<4; i++)
			if(i==ans1-1)
				for (int j = 0; j<4; j++)
						cin >> num1[j];
			else
				for (int j = 0; j<4; j++)
					cin >> dummy;
					
	
		cin >> ans2;
		for(int i = 0; i<4; i++)
			if(i==ans2-1)
				for (int j = 0; j<4; j++)
						cin >> num2[j];
			else
				for (int j = 0; j<4; j++)
					cin >> dummy;
		
		int count = 0, index = -1;
		for(int i = 0; i <4; i++)
			for (int j = 0; j<4; j++)
				if(num1[i]==num2[j])
				{
					count++;
					index = j;
				}

		cout << "Case #" << (t + 1) << ": ";
		if(count == 1) 
			cout <<  num2[index] << "\n";
		else if (count == 0)
			cout <<  VOLUNTEER_CHEATED << "\n";	
		else
			cout <<  BAD_MAGICIAN << "\n";	

	}

	fclose(stdout);
	fclose(stdin);
	return 0;
}