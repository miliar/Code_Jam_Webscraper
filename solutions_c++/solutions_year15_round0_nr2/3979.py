//Kyle Hatfield
//email ktbh4jc@gmail.com
//April 11 2015
//ihop
#include <iostream>
#include <math.h>
using namespace std;
int main()
{
	const int INIT_TO_ZERO = 0;
	int num_plates, plate_value, num_cases, tallest_stack, working_cost, down, cost;
	int stacks [1001];
	cin >> num_cases;
	for(int x=INIT_TO_ZERO; x < num_cases; x++)
	{
	//	cout << "--------------------------case:" << x+1 << "--------"<< endl;
		tallest_stack=INIT_TO_ZERO;
		for(int y = INIT_TO_ZERO; y < 1001; y++)
			stacks[y] = INIT_TO_ZERO;
		cin >> num_plates;
		for(int k = INIT_TO_ZERO; k< num_plates; k++)
		{
			cin >> plate_value;
			stacks[plate_value]++;
			if (plate_value > tallest_stack)
				tallest_stack=plate_value;
		}
		cost = 999999999;
		for (int i = 1; i <= tallest_stack; i++)
		{
			working_cost = i; 
			for (int j = INIT_TO_ZERO; j < tallest_stack+1; j++)
			{
				if(stacks[j] != INIT_TO_ZERO)
				{
				if(i>j)
					down = INIT_TO_ZERO;
				else
					down=ceil(j/static_cast<float>(i))-1;
		//		cout << "j=" << j << endl;
		//		cout << "i=" << i << endl;
		//		cout << "down = " << down << endl;
		//		cout << "working_cost before =" << working_cost << endl;
				working_cost += down*stacks[j];	
		//		cout << "working_cost after =" << working_cost << endl;
				}
			}
		//	cout << "cost before" << cost << endl;
			if(working_cost < cost)
				cost = working_cost;
		//	cout << "cost after" << cost << endl;
		}
		cout << "Case #" << x+1 << ": " << cost << endl;
	}
	return INIT_TO_ZERO;
}