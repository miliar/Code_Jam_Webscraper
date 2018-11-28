
#include<iostream>
#include<string>
#include<fstream>
using namespace std;

void main()
{ ifstream inputfile;
  inputfile.open ("input.txt");
  ofstream outputfile;
  outputfile.open ("output.txt");
  int number_of_test_cases;
  inputfile>>number_of_test_cases;
  //unsigned short *input;
  string mystring;
  unsigned short number_of_friends_added=0,total=0;
  unsigned short input_length=0;
  int temp=0;

  for(unsigned short j=0;j<number_of_test_cases;j++)
	{
		inputfile>>input_length;
		input_length++;
		inputfile>>mystring;



//take input into array 
//and get size of array by getting the length of the string -2

//input=new unsigned short[input_length];



number_of_friends_added=0;total=0;
for(unsigned short i=0;i<input_length;i++)
	{	temp=int(mystring[i])-'0';
		if(total<i)
		{
		number_of_friends_added+=i-total;
		total=temp+i;
		
		}
		else
		{total+=temp;}

}
outputfile<<"Case #"<<j+1<<": "<<number_of_friends_added<<endl;

  }
  


}
