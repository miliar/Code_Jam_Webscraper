#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(){
	ofstream fout("output");
	ifstream fin("A-small-attempt4.in");
	int testNum = 0;
	fin>>testNum;
	int thisRoundid = 0;
	string* result=new string[testNum];
	while(thisRoundid < testNum)
	{
		if(thisRoundid == 3)
		{
			int test=0;
		}
		char plate[4][4]={} ;
		//1. fill the plate
		for(int i =0 ; i< 4; i++)
		{
			string row="";
			fin>>row;
			if(row.length()>4)
				return 1;
			//plate[i]=row.c_str();
			memcpy(plate[i], row.c_str(), 4); // string to char[]
		}

		//2.judge if there is some won
		//2.1 X or O won
		char label[2]={'X','O'};
		for(int t=0;t<2;t++)
		{
			int score1=0;//zheng dui jiao
			int score2=0;//fu dui jiao
			//row
			for(int i=0;i<4;i++)
			{	
				if(plate[i][i] == label[t] || plate[i][i] == 'T')
					score1++;
				if(plate[i][3-i] == label[t] || plate[i][3-i] == 'T')
					score2++;
				int rowscore = 0;
				int colscore = 0;
				for(int j=0;j<4;j++)
				{
					if (plate[i][j] == 'T' || plate[i][j]==label[t])
						rowscore ++;
					if (plate[j][i] == 'T' || plate[j][i]==label[t])
						colscore ++;
				}
				if (rowscore == 4 || colscore == 4 )
				{
					result[thisRoundid] = "  won";
					result[thisRoundid][0]=label[t];
					break;
				}
			}
			if(result[thisRoundid].length()>0)
			{
				break;
			}
			if (score1 == 4 || score2 == 4 )
			{
				result[thisRoundid] = "  won";
				result[thisRoundid][0]=label[t];
				break;
			}

		}
		if(result[thisRoundid].length()>0)
		{
			thisRoundid ++;
			continue;
		}		
		//2.3 not complete
		for(int i = 0; i<4;i++)
		{
			for(int j=0; j<4; j++)
			{
				if(plate[i][j] == '.')
				{
					result[thisRoundid] = "Game has not completed";
					break;
				}
			}
			if(result[thisRoundid].length()>0)
				break;
		}
		if(result[thisRoundid].length()>0)
		{
			thisRoundid++;
			continue;
		}
		//2.4 draw
		result[thisRoundid] ="Draw"; 
		thisRoundid ++;
	}
	for(int i=0; i< testNum; i++)
	{
		fout<<"Case #"<<i+1<<": "<<result[i]<<endl;
	}

	return 0;
}