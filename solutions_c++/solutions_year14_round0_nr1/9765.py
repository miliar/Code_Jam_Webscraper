#include <iostream>
#include <fstream>


using namespace std;
int main()
{
	ifstream input("A-small-attempt0.in");
	ofstream output("output.txt");
	
	int tests;
	int cards[4][4][2];
	int found;
	int number;
	
	input >> tests;
	for(int i = 0; i < tests; i++)
	{
		found = 0;
		number = 0;
	    int first;
	    input >> first;
	    for(int r = 0; r < 4; r++)
	    {
	        for(int c = 0; c < 4; c++)
	        {
	            input >> cards[r][c][0];
	        }
	    }
	    
	    int second;
	    input >> second;
	    for(int r = 0; r < 4; r++)
	    {
	        for(int c = 0; c < 4; c++)
	        {
	            input >> cards[r][c][1];
	        }
	    }
	    
	    for(int m = 0; m < 4; m++)
	    {
	        for(int mm = 0; mm < 4; mm++)
	        {
	        	//cout << cards[first-1][m][0] << "-" << cards[second-1][mm][1] << "/";
	            if(cards[first-1][m][0] == cards[second-1][mm][1])
	            {
	                if(found == 0)
	                {
	                    number = cards[first-1][m][0];
	                }
	                found++;
	            }
	        }
	        //cout << endl;
	    }
	    
	    cout << found << endl;
	    if(found == 1)
	    {
	        output << "Case #" << i + 1 << ": " << number << endl;
	    }
	    else if(found > 1)
	    {
	    	output << "Case #" << i + 1 << ": Bad magician!"<< endl;
	    }
	    else if(found == 0)
	    {
	    	output << "Case #" << i + 1 << ": Volunteer cheated!" << endl;
	    }
	    
	}
}
