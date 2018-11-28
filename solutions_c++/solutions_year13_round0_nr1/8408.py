#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
using namespace std;

char r[4], c[4], d[4]; 
//4-rows, 4-columns, 2-diagonals (+2 dummy diagonal)

void init_rcd(void);
void calcNextStatus(char*, char);
void calcResult(int n);
void showAll(void);

int main(int argc, char *argv[])
{
	string line;
	int T;
	
	cout<<argv[1]<<endl;
	ifstream fin(argv[1]);
	
	getline(fin, line);
	T = atoi(line.c_str());

	for (int n=0; n<T; n++)
	{
		init_rcd();		
		
		for(int i=0; i<4; i++)
		{
			getline(fin,line);
			cout<<line<<endl;
			
			for (int j=0; j<4; j++)
				{
					// if 'T' values stay the same
					if (line[j]!='T')
					{
						calcNextStatus(&r[i],line[j]);
						calcNextStatus(&c[j],line[j]);
						if (j==i) calcNextStatus(&d[0],line[j]);
						if ((i+j)==3) calcNextStatus(&d[1],line[j]);
					}						
				}		
			//showAll();
		}
		
		calcResult(n);
		getline(fin, line);//empty line
		//cout<<endl;
	}

	fin.close();
	
	return 0;
}

void init_rcd(void)
{
	for (int i=0; i<4; i++)
		r[i] = c[i] = d[i] = ' ';			
}

void calcNextStatus(char *myC, char nextC)
{
	if (*myC==' ')
		*myC = nextC;
	else if (nextC=='.')
		*myC = '.';
	else if (*myC!=nextC)
		*myC = 'D'; 					
}

void calcResult(int n)
{
	ofstream fout("myoutput.out", ios::app);
	
	string result = "Draw";
	
	for (int i=0; i<4; i++)
	{
		if ((r[i] == '.') || (c[i] == '.') || (d[i] == '.'))
			result = "Game has not completed";
		
		if ((r[i] == 'X') || (c[i] == 'X') || (d[i] == 'X'))
		{		
			result = "X won";
			//cout<<i<<" - "<<r[i]<<c[i]<<d[i]<<endl;
			break;
		}	
		 
		if ((r[i] == 'O') || (c[i] == 'O') || (d[i] == 'O'))
		{	
			//cout<<i<<" - "<<r[i]<<c[i]<<d[i]<<endl;		
			result = "O won";
			break;
		} 			
	}		
	
	cout<<"Case #"<<n+1<<": "<<result<<endl;
	fout<<"Case #"<<n+1<<": "<<result<<endl;
	
	fout.close();
	
}

void showAll(void)
{
	for (int i=0; i<4; i++)
	cout<<i<<" - "<<r[i]<<c[i]<<d[i]<<endl;
}

