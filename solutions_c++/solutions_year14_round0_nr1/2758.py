#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <stdint.h>
#include <ctime>
#include <cstdlib>
#include <cmath>
#include <sstream>
#include <stdio.h>

using namespace std;


int main()
{
	int T;
	
	cin>>T;
	
	for (int i=0; i<T; i++)
	{
		int guess1, guess2;
		cin >> guess1;
		int temp;
		vector<int> s1,s2;
		for (int j=0; j<4; j++)
		{
			for (int k=0; k<4; k++)
			{
				cin >> temp; 
				if (j+1==guess1)
				{
					s1.push_back(temp);
				}
			}
		}
		cin >> guess2;
		for (int j=0; j<4; j++)
		{
			for (int k=0; k<4; k++)
			{
				cin >> temp; 
				if (j+1==guess2)
				{
					s2.push_back(temp);
				}		
			}
		}
		
		vector<int> res;
		for (int j=0; j<4; j++)
		{
			for (int k=0; k<4; k++)
			{
				if (s1[j]==s2[k])
				{
					res.push_back(s1[j]);
				}
			}
		}
		//cout << "so far so good " << guess1 << " " << guess2 << endl;
				
		switch(res.size())
		{
			case 1: 
				printf("Case #%d: %d\n", i+1, res[0]);
				break;
			case 0:
				printf("Case #%d: Volunteer cheated!\n", i+1);
				break;
			default:
				printf("Case #%d: Bad magician!\n", i+1);
		}
		
		
	}

}
