#include <iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		char inputs[1003] = {0};
		char outputs[4000] = {0};
		cin >> inputs;
		
		int j = 1;
		int front = 1003;
		int end = 1003;
		
		outputs[end] = inputs[0];
		end++;
		
		while(inputs[j] >= 'A' && inputs[j] <='Z' && j < 1003)
		{
			if(inputs[j] < outputs[front])
			{
				outputs[end] = inputs[j];
				end++;
			}
			else
			{
				front--;
				outputs[front] = inputs[j];

			}
			j++;
		}
		cout << "Case #" << i + 1 << ": ";
		for(int k = 0; k < 4000; k++)
		{
			if(outputs[k] != 0)
			{
				cout << outputs[k];
			}
		}
		cout << endl;
	}
}
