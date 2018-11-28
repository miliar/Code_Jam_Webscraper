#include <stdio.h>
#include <conio.h>
#include <climits>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solve(int a, vector<vector<int>> A, int b, vector<vector<int>> B , int &val)
{
	vector<int> first = A[a-1];

	vector<int> second = B[b-1];
	int i = 0;
	for(vector<int>::iterator itA = first.begin(); itA!= first.end(); itA++)
	{
		for(vector<int>::iterator itB = second.begin(); itB != second.end(); itB++)
		{
			if(*itA == *itB)
			{
				val = *itA;
				i++;
			}
		}
	}
	return i;
}

int main()
{
	unsigned short int testcases;
	int a, b, t;
	
    cin >> testcases;
	
    for(int i=1; i <= testcases; i++) 
	{ 
		cin >> a;
		vector<vector<int>> B, A;

        for(int x = 0; x<4; x++)
		{
			//vector<vector<int>> A;
			 
				vector<int> v;
				for(int z = 0; z<4; z++)
				{ 
					cin >> t ;
					v.push_back(t);
				}
				A.push_back(v);
								
			
			
		}

		cin >> b;
		 for(int x = 0; x<4; x++)
		{
			
				vector<int> v;
				for(int z = 0; z<4; z++)
				{ 
					cin >> t ;
					v.push_back(t);
				}
				B.push_back(v);
								
			
			
		}


		int val;
		int ans = solve(a, A,b, B, val);
		if(ans == 0)
			printf("Case #%d: Volunteer cheated!\n", i);
		else if ( ans > 1)
			printf("Case #%d: Bad magician!\n", i);
		else
			printf("Case #%d: %d\n", i, val);
        
    }

	getch();
}