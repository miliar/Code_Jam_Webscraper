#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>
 
using namespace std;
 
int main()
{
    int cases;
     
    while(cin >> cases)
    {
    	for (int i = 0; i < cases; ++i)
        {
            int first, second;
            int first_position[4][4];
            int second_position[4][4];
            vector<int> first_row;
            int total = 0;
            int answer;

            cin >> first;

            for (int j = 0; j < 4; ++j)
            {
                for (int k = 0; k < 4; ++k)
                {
                    cin >> first_position[j][k];
                }
            }

            for (int j = 0; j < 4; ++j)
            {
                first_row.push_back(first_position[first-1][j]);
            }

            cin >> second;

            for (int j = 0; j < 4; ++j)
            {
                for (int k = 0; k < 4; ++k)
                {
                    cin >> second_position[j][k];
                    
                    if(j == second-1)
                    {
                        if(find(first_row.begin(), first_row.end(), second_position[j][k]) != first_row.end())
                        {
                            total++;
                            answer = second_position[j][k];
                        }
                    }
                }
            }
            
            cout << "Case #" << i+1 << ": ";

            if(total == 1)
                cout << answer;
            else if(total > 1)
                cout << "Bad magician!";
            else if(total < 1)
                cout << "Volunteer cheated!";
            
            cout << endl;
        }
        
    }
     
    return 0;
}