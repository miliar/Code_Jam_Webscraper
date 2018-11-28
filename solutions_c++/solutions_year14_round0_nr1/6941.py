
#include <assert.h>
#include <fstream>

using namespace std;


int main()
{
	  std::ifstream infile("D:/input.txt");
	  int testCases=0;
	  
	  infile >>testCases;
	  int i=0;
	  int first=0;
		  int second=0;
		  infile >>first;
		  ofstream outfile;
		  outfile.open ("D:/output.txt");
		  
		  
      while(i<testCases)
	  {
		  
		  int row11=0;
		  int row12=0;
		  int row13=0;
		  int row14=0;
		  int row21=0;
		  int row22=0;
		  int row23=0;
		  int row24=0;
		  int sum=0;
		  int choosen=0;
		  int rest=0;
		  for(int i=0 ; i<first;i++)
		  {
			 infile >>row11 >>row12>>row13>>row14;
			 rest=4-i-1;
		  }
		  for(int i=0;i<=rest*4;i++)
			infile >>second;
		  for(int i=0 ; i<second;i++)
		  {
			 infile >>row21 >>row22>>row23>>row24;
			 rest=4-i-1;
		  }
		  if(row11==row21||row11==row22||row11==row23||row11==row24)
		  {
			  sum++;
			   choosen=row11;
		  }
		   if(row12==row21||row12==row22||row12==row23||row12==row24)
		  {
			  sum++;
			   choosen=row12;
		  }
		  if(row13==row21||row13==row22||row13==row23||row13==row24)
		  {
			  sum++;
			   choosen=row13;
		  }
		  if(row14==row21||row14==row22||row14==row23||row14==row24)
		  {
			  sum++;
			  choosen=row14;
		  }
		  if(sum==0)
			outfile << "Case #"<<i+1<<": "<<"Volunteer cheated!\n";

		  else if(sum>1)
		  {
			  
			  outfile << "Case #"<<i+1<<": "<<"Bad magician!\n";
		  }
		  else
			  outfile << "Case #"<<i+1<<": "<<choosen<<"\n";
		  
		  i++;
		  for(int i=0;i<=rest*4;i++)
			infile >>first;
      }
    outfile.close();
	return 0;
}