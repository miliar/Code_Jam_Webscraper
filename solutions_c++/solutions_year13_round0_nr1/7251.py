
#include <iostream>
#include <string>
#include <fstream>
using namespace std;


int main()
{
	char map[4][4];
	int n;
	 ofstream output;
	//ifstream myfile ("example.txt");
	//myfile.open ("example.txt");
   output.open ("output.txt");
   //output << "Writing this to a file.\n";
  
	string line;
	/*if (myfile.is_open())
  {
    while ( myfile.good() )
    {*/
      //getline (myfile,line);
	 // n= atoi(line.c_str());
    cin >>n;
	string value;
	for (int i=0; i<n; i++)
	{
		bool dot = false;
		//kol mara haida5al 4 test case 
		for(int j=0; j<4; j++)
		{
			//getline (myfile,value);
			cin>> value;
			for (int k=0; k<4 ; k++)
			{
				if (value[k] == '.')
				{
					dot = true;
				}
				map[j][k] = value[k];
			}
		}
		bool won = false;
		// hena el mafrood el check 3lshan el output
		if (((map[0][0] == map[1][1])&& (map[2][2] == map[3][3]) &&(map[1][1] == map[3][3]) && (map[1][1] != '.'))||( (map[0][0] == map[1][1]) &&(map[1][1] == map[2][2]) &&( map[3][3] =='T')&& (map[1][1] != '.')) || ((map[0][0] == map[1][1]) &&(map[1][1]== map[3][3]) && (map[2][2] == 'T') && (map[1][1] != '.')) ||((map[0][0] == map[2][2]) &&(map[2][2] == map[3][3]) &&(map[1][1] == 'T') && (map[2][2] != '.')) ||( (map[1][1] == map[2][2]) &&(map[2][2] == map[3][3]) && (map[0][0] ==  'T') && (map[1][1] != '.')))
		{
			if (map[0][0] != 'T')
			{
				output << "Case #"<< (i+1) <<": "<< map[0][0]<<" won" <<endl;
			}
			else
			{
				output << "Case #"<< (i+1) <<": "<< map[1][1]<<" won" <<endl;
			}
			won = true;
		}
		else if (((map[0][3] == map[1][2])&& (map[2][1] == map[3][0]) &&(map[1][2] == map[3][0]) && (map[1][2] != '.'))||( (map[0][3] == map[1][2]) &&(map[1][2] == map[2][1]) &&( map[3][0] =='T')&& (map[1][2] != '.')) || ((map[0][3] == map[1][2]) &&(map[1][2]== map[3][0]) && (map[2][1] == 'T') && (map[1][2] != '.')) ||((map[0][3] == map[2][1]) &&(map[2][1] == map[3][0]) &&(map[1][2] == 'T') && (map[2][1] != '.')) ||( (map[1][2] == map[2][1]) &&(map[2][1] == map[3][0]) && (map[0][3] ==  'T') && (map[1][2] != '.')))
		{
			if (map[0][3] != 'T')
			{
				output << "Case #"<< (i+1) <<": "<< map[0][3]<<" won" <<endl;
			}
			else
			{
				output << "Case #"<< (i+1) <<": "<< map[1][2]<<" won" <<endl;
		
			}
			won = true;
		}
		
		else
		{
			for (int l=0; l<4;l++)
			{
				 if ((map[l][0] == map[l][1]) && (map[l][2] == map[l][3]) &&(map[l][1] == map[l][3]) && (map[l][1] != '.') )	{
					output << "Case #"<< (i+1) <<": "<< map[l][0]<<" won" <<endl;
					won = true;
					break;
				}
				 else if ((map[l][0] == map[l][1]) &&(map[l][1] == map[l][2]) && (map[l][3] =='T')  && (map[l][1] != '.')) 
				 {
					 output << "Case #"<< (i+1) <<": "<< map[l][0]<<" won" <<endl;
					won = true;
					break;
				 }
				 else if ((map[l][0] == map[l][1]) && (map[l][1]== map[l][3]) && (map[l][2] == 'T')  && (map[l][1] != '.')) 
				 {
					 output << "Case #"<< (i+1) <<": "<< map[l][0]<<" won" <<endl;
					won = true;
					break;
				 }
				 else if((map[l][0] == map[l][2]) && (map[l][2] == map[l][3]) && (map[l][1] == 'T')  && (map[l][2] != '.')) 
				 {
					 output << "Case #"<< (i+1) <<": "<< map[l][0]<<" won" <<endl;
					won = true;
					break;
				 }
				 else if((map[l][1] == map[l][2]) && (map[l][2] == map[l][3]) && (map[l][0] ==  'T')  && (map[l][1] != '.'))
				 {
					 output << "Case #"<< (i+1) <<": "<< map[l][2]<<" won" <<endl;
					won = true;
					break;
				 }
				else  if (((map[0][l] == map[1][l]) && ( map[2][l] == map[3][l]) && (map[1][l] == map[3][l]) && (map[1][l] != '.'))|| ((map[0][l] == map[1][l]) &&(map[1][l] == map[2][l]) && (map[3][l] =='T') && (map[1][l] != '.')) || ((map[0][l] == map[1][l]) &&(map[1][l]== map[3][l]) && (map[2][l] == 'T') && (map[1][l] != '.')) ||((map[0][l] == map[2][l]) &&(map[2][l] == map[3][l]) && (map[1][l] == 'T') && (map[2][l] != '.')) || ((map[1][l] == map[2][l]) && (map[2][l] == map[3][l]) && (map[0][l] ==  'T') && (map[1][l] != '.')))
				{
					if (map[0][l] != 'T')
					{
						output << "Case #"<< (i+1) <<": "<< map[0][l]<<" won" <<endl;
					}
					else
					{
						output << "Case #"<< (i+1) <<": "<< map[2][l]<<" won" <<endl;
		
					}
						won = true;
						break;
				}
			}
			if (won == false)
			{
				if (dot == true)
				{
					output << "Case #"<< (i+1) <<": "<<"Game has not completed" <<endl;
				}
				else
				{
					output << "Case #"<< (i+1) <<": "<<"Draw" <<endl;
				}
			}
		}
		
	}
	
	  //myfile.close();
	  output.close();
	return 0;
}