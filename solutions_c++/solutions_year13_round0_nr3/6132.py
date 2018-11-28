#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <cmath>
using namespace std;


bool ifpdrome(int num);
string convertInt(int num);

string convertInt(int number)
{
   stringstream ss;
   ss << number;
   return ss.str();
}

bool ifpdrome(int num)
{
  bool result;
 
  if(num<10)
  {
  	result=true;
  	return result;
  }
 
 	string curnum=convertInt(num);
 	int length= curnum.length();
	//cout << "num is" << num << "length is " << length <<endl;
	int poscheck=floor(length/2);
	for(int i=0; i<poscheck; i++)
	{
		int endindex=length-1-i;
		if(curnum[i]!=curnum[endindex])
		{
			result=false;
			break;
		}else{

			result=true;
		}

	}

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


for(int i=0;i<case_num;i++)
{
	
	int lower,upper,result=0;
	bool myresult,sqrresult;
	inputfile>>lower;
	inputfile>>upper;

	for(int j=lower;j<=upper;j++)
	{
		int num=j;
		int root=sqrt(num);
		if((root-sqrt(num))==0)
		{
			sqrresult= ifpdrome(sqrt(num));
			myresult = ifpdrome(num);
	
			if(myresult==true&&sqrresult==true)
			{
				result++;
			}

		}	
		

	}	
	

  	
  	cout<< result << endl;
  	string result1="Case #";
  	 ostringstream ss,ss1;
      ss << i+1;
      ss1<< result;
     string stri= ss.str();
     string strresult=ss1.str();
  	result1.append(stri);
 	result1.append(": ");
  	result1.append(strresult);
  	result1.append("\n");
	 outputfile<< result1;
}

  	inputfile.close();
	outputfile.close();

	return 0;
}










