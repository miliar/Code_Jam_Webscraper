#include <iostream>
#include <string>
#include<vector>

//using std::string;
//using std::cin;
//using std::cout;
//using std::endl;

using namespace std;
int main()
{
	int T;
	int pos1,pos2, card;
	int originalArray[4][4];
	int modifiedArray[4][4];
	char buffer[33];
	char buffer2[33];
	std::string str1,str2,str3;
	std::vector<string> output;	
	bool isSame = false;
	cin >> T;
	int row,col;

	for(int i = 0; i < T; i++)
	{
		//itoa (i+1,buffer,10);
		row = -1;
		col = -1;		
		int count = 0;		
		cin >> pos1;
		pos1 = pos1-1;
		for(int j = 0;j < 4;j++)
		{
			
			for(int k = 0; k < 4; k++)
			{
				cin >> card;	
				originalArray[j][k] = card; 
			}

		}
		cin >> pos2;
		pos2 = pos2-1;
		for(int j = 0;j < 4;j++)
		{
			
			for(int k = 0; k < 4; k++)
			{
				cin >> card;	
				modifiedArray[j][k] = card; 
			}

		}
		for(int j = 0;j < 4;j++)
		{
			//cout << "Checking row " << pos1 <<" "<<pos2;
			for(int k = 0; k < 4; k++)
		{
			if(originalArray[pos1][j] == modifiedArray[pos2][k])
			{	
				//cout << "Test case : " << i+1 << endl;				
				//cout <<"Common elements of rows are " << originalArray[pos1][j];
				count ++;
				if((row == -1) && (col == -1))
				{	
					row = pos1;
					col = j;
				}					
				//cout << "Count = " << count; 
			}
		}			

		}
		if(count == 1)
		{	
			//cout << "Entered count!" << endl;		
			str1 = "Case #" + to_string(i+1) + ": " + to_string(originalArray[row][col]);
			output.push_back(str1);
		}
		if(count > 1)
		{	
			str2 =  "Case #" + to_string(i+1) + ": " + "Bad magician!" ;
			output.push_back(str2);
}
		if(count == 0 )
		{	
			str3 = "Case #" + to_string(i+1) + ": " + "Volunteer cheated!";
			output.push_back(str3);
		}

			
		/*if(isSame)
		{
			//string num = i.c_str();
			if(pos1 == pos2)
				str =  "Case #" + to_string(i+1) + ": " + "Bad magician!\n" ;
			if(( pos1!=pos2 ) || ( pos1 > 4 )|| ( pos2 > 4 ) )
				str = "Case #" + to_string(i+1) + ": " + "Volunteer cheated!\n";
		}
		else
		{
			//itoa(originalArray[pos1][pos2],buffer2,10);
			//str = "Case #" + string(i+1) + ": " + buffer2 + "\n";
			str = "Case #" + to_string(i+1) + ": " + to_string(originalArray[pos1][pos2]);
		}
		*/
				
		
		




	}
	for (std::vector<string>::iterator it = output.begin(); it != output.end(); ++it)
	{
		cout << (*it) << "\n";
		

	}



}
