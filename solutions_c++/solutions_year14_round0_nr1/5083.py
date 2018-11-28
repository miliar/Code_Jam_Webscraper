#include <iostream>
#include <fstream>
using namespace std;


int main()
{
	int testcase;
	int array[2][16];
	int index[2];

	
	ifstream input("input1.in",ios::in);
	ofstream output("output.out",ios::out|ios::app);
	
	input>>testcase;
	
	for (int i=0;i<testcase;i++)
	{
		int match = 99;
		bool finish = false;
		for(int j=0;j<2;j++)
		{
			input>>index[j];
	
			for (int k=0;k<16;k++)
				input>>array[j][k];
		}
		
		for (int a=(index[0]-1)*4;a<index[0]*4;a++)
		{
			for (int b=(index[1]-1)*4;b<index[1]*4;b++)
			{
				if (array[0][a] == array[1][b])
				{
					if (match == 99) {
						finish = false;
						match = array[0][a];
						break;
					}
					else if (match !=99)
					//there is other matched value
					{
						finish = true;
						break;
					}
				}
					
			}
			if (a == index[0]*4-1  && finish ==false)
			{
				if (match == 99)
					output<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
				else
					output<<"Case #"<<i+1<<": "<<match<<endl;		
			}

			if (finish == true) {
				output<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
				break;
            }
		}
    }
	input.close();
	output.close();

}

