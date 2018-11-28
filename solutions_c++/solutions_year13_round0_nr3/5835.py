#include <iostream>;
#include <string>;
#include <sstream>;
#include <cmath>;
#include <math.h>

using namespace std;

int main()
{
	int cases;
	cin>>cases;
	int temp2 = cases;
	int temp3=0 ;

	int number,number_two,tempe;
	while(cases!=0)
	{
		temp3=temp2-cases+1;
		cin>>number;
		cin>>number_two;
		tempe = number_two +1;
		int counter=0;

		
	while(number!=tempe)
		{
		ostringstream convert;   
		ostringstream convert_two; 
		convert << number;      
		string result = convert.str();
		string second_number;
		int length = result.length();
		int mid = length/2;
		int flag=0;

		for(int i=0;i<mid;i++)
		{
			int temp = length-i-1;
			if(result[i]!=result[temp])
			{
				flag=1;
				goto found;
				
			}
		}


		double num = number;
		double square_root =sqrt(num);

		

		convert_two<<square_root;
		

		second_number =  convert_two.str();

		int new_length = second_number.length();
		double  fractpart, intpart;
		fractpart = modf (square_root , &intpart);

		if(fractpart>0)
		{
			goto found;
		}
		
		mid = new_length/2;

		for(int i=0;i<mid;i++)
		{
			int temp = new_length-i-1;
			if(second_number[i]!=second_number[temp])
			{
				
				goto found;
				
			}
		}

		counter++;

		found:

		number++;
		}
	cout<<"Case #"<<temp3<<": "<<counter<<endl;
		cases--;
	}

	
	
	
return 0;
}