#include <iostream>
#include <string>
#include <cstdio>
#include <sstream>
#include <vector>

using namespace std;

int main()
{
	int cases;
	cin >> cases;

	for (int i = 0; i < cases; ++i)
	{
		int level; 
		cin >> level;
		level++;

		string scale;
		cin >> scale;
        // printf("#%s#\n", scale.c_str());

        vector<int> shyness(level, 0);

		for ( int k = 0; k < level; k++ )
        {
            int input = atoi(string(1, scale[k]).c_str()) + shyness[k];
            int j = 0;
            shyness[k] = 0;
            for (; input > 0 && j + k < level; input--, j++ )
            {
                shyness[k + j] += 1;
            }
            if ( input > 0 )
            {
                shyness[k + j - 1] += input;
            }
        }

        int counter = 0;
        for (int k = 0; k < level; ++k)
        {
        	if (shyness[k] == 0)
        	{
        		counter++;
        	}
        }
        // cout << counter << endl;
        printf("Case #%d: %d\n", i + 1, counter );
	}
}