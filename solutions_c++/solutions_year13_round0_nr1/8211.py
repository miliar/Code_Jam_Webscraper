#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>

using namespace std;

int main()
{
    ifstream fin("A-small-input.in");
    ofstream fout("A-small-input.out");
   
    int T;
    
    fin >> T;
    
    for(int p=0 ; p<T ;p++)
    {
			char arr[4][4];
			char firstchar;
			int win=0;
			bool cols=true,rows=true;

			for(int i=0;i<4;i++){
				for(int j=0;j<4;j++){
					fin>>arr[i][j];
				}
			}

			// check for rows 
           for(int i=0;i<4;i++)
		   {
			   win=0;
			   if(arr[i][0]=='T')
				firstchar==arr[i][1];
				else
			    firstchar=arr[i][0];
			   for(int j=0;j<4;j++)
			   {
				  			   
				   if(firstchar=='.')
					   break;
					if(arr[i][j+1]==firstchar||arr[i][j+1]=='T')
					{
						win++;
					}
					else break;
			   }
			   if(win>=3)
			   { 
				   if(firstchar=='X')
				   {
					   fout << "Case #" << p+1 << ": " <<"X won"<< endl;
					   goto end;
				   }
				   else if(firstchar=='O')
				   {
					   fout << "Case #" << p+1 << ": " <<"O won"<< endl;
						goto end;
				   }
			   }
			   else
			   {
				   rows=false;
			   }
		   }

		  
		   // check for coloums 
           for(int i=0;i<4;i++)
		   {
			   win=0;
			   if(arr[0][i]=='T')
				firstchar==arr[1][i];
				else
			   firstchar=arr[0][i];
			   for(int j=0;j<4;j++)
			   {
					if(firstchar=='.')
					   break;

					if(arr[j+1][i]==firstchar||arr[j+1][i]=='T')
					{
						win++;
					}
					else break;
				}

			   if(win>=3)
			   { 
					if(firstchar=='X')
				   {
					   fout << "Case #" << p+1 << ": " <<"X won"<< endl;
					   goto end;
				   }
				   else if(firstchar=='O')
				   {
					   fout << "Case #" << p+1 << ": " <<"O won"<< endl;
						goto end;
				   }
			   }
			   else
			   {
				   cols=false;
			   }
		   }

		   //Check diagonals
		   if(arr[0][0]=='T')
			firstchar==arr[1][1];
		   else
		   firstchar=arr[0][0];
		   if((arr[1][1]==firstchar||arr[1][1]=='T')&&
			  (arr[2][2]==firstchar||arr[2][2]=='T')&&
			  (arr[3][3]==firstchar||arr[3][3]=='T'))
		   {
				if(firstchar=='X')
				   {
					   fout << "Case #" << p+1 << ": " <<"X won"<< endl;
					   goto end;
				   }
				   else if(firstchar=='O')
				   {
					   fout << "Case #" << p+1 << ": " <<"O won"<< endl;
						goto end;
				   }
		   }
		   if(arr[0][3]=='T')
			firstchar==arr[1][2];
		   else
		    firstchar=arr[0][3];
		   if((arr[1][2]==firstchar||arr[1][2]=='T')&&
			  (arr[2][1]==firstchar||arr[2][1]=='T')&&
			  (arr[3][0]==firstchar||arr[3][0]=='T'))
		   {
				if(firstchar=='X')
				   {
					   fout << "Case #" << p+1 << ": " <<"X won"<< endl;
					   goto end;
				   }
				   else if(firstchar=='O')
				   {
					   fout << "Case #" << p+1 << ": " <<"O won"<< endl;
						goto end;
				   }
		   }
		   // Know draws or lose 
		   for(int i=0;i<4;i++)
		   {
			   for(int j=0;j<4;j++)
			   {
				   if(arr[i][j]=='.')
				   {
					    fout << "Case #" << p+1 << ": " <<"Game has not completed"<< endl;
						goto end;
				   }
			   }
		   }
		   
		   //draws
		   if((!rows)&&(!cols))
		   fout << "Case #" << p+1 << ": " <<"Draw"<< endl;
		   end:;
    }
	return 0;
}