//name Yufei Wang

#include <iostream>
#include <fstream>
#include <stdlib.h> 
#include <iomanip>

using namespace std;

int main (int arg, char* argv[])
{
	
	int numofrun = 0;
	int currentrun = 1;
	double goal;
	double increasR;
	double Cost;

	double b1,b2;
	double x1,x2;
	double t1,t2;
	int numofhouse = 0;
	double temp = 0;

	double answer = 0;
///////////////////get the code from file/////////
	string filename;
	ifstream infile;
	ofstream outfile;
	infile.open(argv[1], ios::in);
	outfile.open("result.txt", ios::out);
	if(!infile)
	 {
	  cout <<" cannot open file" ;
	  exit(0);
	  }

	if(!outfile)
	{
	  cout <<" cannot open file" ;
	  exit(0);
	 }

infile >> numofrun; ///number of tests

	 while( currentrun<= numofrun)
{
	infile >> Cost;
	
	infile >> increasR;
	
	infile >> goal;


///////////////////////end of getting data, now calculation///////////
numofhouse = 0;
x1 = goal/2;
x2 = goal/(2+increasR);
b1 = Cost/2;
b2 = Cost/(2+increasR) + b1;
t1 = x1;
t2 = b1 + x2;

while(t1>t2)
{
	numofhouse++;
	//cout<<t1<<" "<<t2<<endl;
	temp = b2;
	b2 = (Cost/(2+(numofhouse+1)*increasR))+b2;
	b1 = temp;

	//cout<<"bbbb"<<b1<<" "<<b2<<endl;
	temp = x2;
	x2 = goal/(2+(numofhouse+1)*increasR);
	x1 = temp;

	temp = t2;
	t2 = x2 + b1;
	t1 = temp;

	//cout<<"xxxx"<<x1<<" "<<x2<<endl;

}


outfile<<"Case #"<<currentrun<<": "<<setprecision(20)<<t1<<endl;








/*
			if(flag == 1)
				outfile<<"Case #"<<currentrun<<": "<<answer<<endl;
			else if (flag ==2)
				outfile<<"Case #"<<currentrun<<": Bad magician!"<<endl;
			else if (flag ==0)
				outfile<<"Case #"<<currentrun<<": Volunteer cheated!"<<endl;
			else
				outfile<<"bug"<<endl;
*/



/*
		outfile <<hex << table[0];
		for (int i = 1; i < 4; ++i)
		{
			if (table[i] != 0)
			{
				outfile <<hex <<" "<< table[i];
			}
		}
		outfile <<endl;
	*/


	
	currentrun++;
}////eof

   infile.close();
   outfile.close();
return 0;
}


