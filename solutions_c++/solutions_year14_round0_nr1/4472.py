#include <iostream>
#include <algorithm>    // std::sort
#include <vector>       // std::vector
#include <fstream>
using namespace std;

int main()
{
	ofstream myfile;
	myfile.open ("magico.txt");

	
	int test, input, count, num, row;
	int grid[4][4];

	cin >> test;
	for (int i = 0; i < test; ++i)
	{
		vector<long> v;
		myfile << "Case #" << i+1 << ": " ;
		cin >> row;
		count = 0;
		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				cin >> input;
				if (j+1==row)
				{
					v.push_back(input);
				}
			}
		}
		cin >> row;
		
		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				cin >> input;
				if(j+1==row){
					if(find(v.begin(), v.end(), input)!=v.end()){
						count++;
						num = input;
					}
				}
				
			}
		}
		if(count == 0){
			myfile << "Volunteer cheated!" << endl;
			
		}else if(count ==1){
			myfile << num << endl;
		}else{
			myfile << "Bad magician!" << endl;
		}
	}

}