#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;
#define row 4


string checkboard(string board[]);
string checkboard (string board[])
{
	bool ifdot;
	bool ift;
	string curelem;
	int numdot = 0; 
	string result="";// Game has not completed
	


	///////horizontal check///////////
	 for(int i=0;i<row;i++)
	 {
	 	string startingelem;
	 	int elesum = 0;	
	 	for(int j=0; j<row;j++)
	 	{	
	 		if(j==0)
	 		{
	 			startingelem=board[i][j];
	 			if(startingelem==".")
	 			{
	 				numdot++;
	 				break;
	 			}

	 		}else{
	 		
	 			curelem= board[i][j];

	 			if(startingelem=="T")
	 			{
	 				startingelem=curelem;
	 			}
	 			if(curelem=="T")
	 			{
	 				curelem=startingelem;
	 			}
	 			if(curelem!=startingelem || curelem==".")
	 			{	 if(curelem==".")
	 				{
	 					numdot++;
	 				}

	 				break;
	 			}else{

	 				elesum++;
	 			}

	 		}
	 	}

	 	if(elesum==3){
	 		result.append(startingelem);
	 		result.append(" won\n");
	 	//	cout<<result;
	 		return result;
	 	}

	 	
	 }
	 /////////////end of horizontal check//////////

	///////vertical check///////////
	 for(int j=0;j<row;j++)
	 {
	 	string startingelem;
	 	int elesum = 0;	
	 	for(int i=0; i<row;i++)
	 	{	
	 		if(i==0)
	 		{
	 			startingelem=board[i][j];
	 			if(startingelem==".")
	 			{
	 				numdot++;
	 				break;
	 			}

	 		}else{
	 		
	 			curelem= board[i][j];

	 			if(startingelem=="T")
	 			{
	 				startingelem=curelem;
	 			}
	 			if(curelem=="T")
	 			{
	 				curelem=startingelem;
	 			}
	 			if(curelem!=startingelem || curelem==".")
	 			{	 if(curelem==".")
	 				{
	 					numdot++;
	 				}

	 				break;
	 			}else{

	 				elesum++;
	 			}

	 		}
	 	}

	 	if(elesum==3){
	 		result.append(startingelem);
	 		result.append(" won\n");
	 	//	cout<<result;
	 		return result;
	 	}

	 	
	 }
	 /////////////end of vertical check//////////


	 /////////////check diag \ side ///////////
	 string startingelem;
	 int elesum = 0;
	 for(int i=0;i<row;i++)
	 {
	 	int j=i;

	 		if(i==0)
	 		{
	 			startingelem=board[i][j];
	 			
	 			if(startingelem==".")
	 			{
	 				numdot++;
	 				continue;
	 			}

	 		}else{
	 			
	 			curelem= board[i][j];

	 			if(startingelem=="T")
	 			{
	 				startingelem=curelem;
	 			}

	 			if(curelem=="T")
	 			{
	 				curelem=startingelem;
	 			}
	 			if(curelem!=startingelem || curelem==".")
	 			{	 if(curelem==".")
	 				{
	 					numdot++;
	 				}

	 				continue;
	 			}else{

	 				elesum++;
	 				
	 			}

	 		}
	 	
	 	if(elesum==3){

	 		result.append(startingelem);
	 		result.append(" won\n");
	 		//cout<<result;
	 		return result;
	 	}
	 }


	 ////////////check the /diagonal
	 elesum = 0;
	 for(int i=0;i<row;i++)
	 {
	 	int j=row-1-i;
	 		if(i==0)
	 		{
	 			startingelem=board[i][j];
	 			if(startingelem==".")
	 			{
	 				numdot++;
	 				continue;
	 			}

	 		}else{
	 			curelem= board[i][j];
	 			
	 			//cout<< curelem<<endl;
	 			if(startingelem=="T")
	 			{
	 				startingelem=curelem;
	 			}
	 			
	 			if(curelem=="T")
	 			{
	 				curelem=startingelem;
	 			}
	 			if(curelem!=startingelem || curelem==".")
	 			{	 if(curelem==".")
	 				{
	 					numdot++;
	 				}

	 				continue;
	 			}else{
	 				elesum++;
	 			}

	 		}

	 	if(elesum==3){
	 		result.append(startingelem);
	 		result.append(" won\n");
	 		//cout<<result;
	 		return result;
	 	}
	 }


	 	if(numdot!=0)
	 	{

	 		result="Game has not completed\n";
	 	}else{

	 		result="Draw\n";
	 	}
	//cout<<result;
	return result;
}



int main (int argc, char *argv[]) {

ifstream inputfile;
ofstream outputfile;
inputfile.open(argv[1]);
outputfile.open("result.txt");
int case_num;
string line;
inputfile>>case_num;
getline(inputfile,line);
	

for(int i=0;i<case_num;i++)
{
	string board[4];
	int temprow=0;

	while(!inputfile.eof())
	{
		getline(inputfile,line);

		 if(line=="")
		 {
		  	break;
		 }

		 board[temprow]=line;
		 temprow++;
	}
		

 	string result= checkboard(board);
 	string result1="Case #";
 	 ostringstream ss;
     ss << i+1;
    string stri= ss.str();
 	result1.append(stri);
 	result1.append(": ");
 	result1.append(result);
 	//cout<<result1;
	outputfile<< result1;
}





// while(!inputfile.eof())
// {
// 	getline(inputfile,line);
// 	stringstream ss(line);
// 	while(getline(ss,item,''))
// 	{
// 		cout<< item << endl;
// 		vec.push_back(item);
// 	}
//  	// cout << vec[0] << endl;
//  	exit(0);
//  }


  	inputfile.close();
	outputfile.close();

	return 0;
}










