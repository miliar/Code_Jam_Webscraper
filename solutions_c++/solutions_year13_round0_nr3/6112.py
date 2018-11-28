//Problem C Fair Square

#include<iostream>
#include<string>
#include<fstream> 
#include<stdio.h>
#include<cmath>


using namespace std; 
int palindrome(long double num);

int main()
{
	string line;
    int numberoftc;
    long double example;
    cout<<"enter example\n";
    example = 1212225222121;
    cout<<"\n enterered number is"<<fixed<<example<<"\n";
	ifstream myfile("C:\\Dev-Cpp\\Workspace\\PD\\input.in");
	ofstream myfileoutput("C:\\Dev-Cpp\\Workspace\\PD\\output.in");

	if(myfile.is_open())
	{
		myfile>>numberoftc;
		cout<<"Number of testcases"<<numberoftc<<"\n";
		long double rangeofnumber[numberoftc*2];
		char ch; 
		long int i = 1;		
		while(!myfile.eof())
		{
			myfile>>rangeofnumber[i];
			myfile>>rangeofnumber[i+1];
			cout<<rangeofnumber[i]<<"\n";
			cout<<rangeofnumber[i+1]<<"\n";
			i=i+2;
		}
		

		for(int count = 1,j=1; count <= numberoftc,j<numberoftc*2; count++,j=j+2)
		{
			int counter = 0;
			for(long double palin_no = rangeofnumber[j]; palin_no <= rangeofnumber[j+1]; palin_no++)
			{
				
				int result = palindrome(palin_no);
				if(result)
				{
					if (!(sqrt(palin_no)-floor(sqrt(palin_no))))
					{
						int result2 = palindrome((sqrt(palin_no)));
						if(result2)
						{
							counter++;
						}
					}
				}
				
			
			}
			cout<<"Case number reached is "<<count<<"\n";
			myfileoutput<<"Case #"<<count<<": "<<counter<<"\n"; 
			
		}
		myfile.close(); 
		myfileoutput.close();
	}
	else 
		cout<<"File not found"<<"\n";
	
	return 0; 	
}
	
int palindrome(long double palin_no)
{
				
	long double sum=0;
	long double r;
    long double temp = palin_no;
	while(temp)
	{
			r=fmod(temp,10);
			temp = floor(temp/10);
			sum = sum*10 + r;
	}			
	if(sum==palin_no)
	{		
	    cout<<"the number is palindrome"<<palin_no<<"\n";
		return 1; 
	}				
	else
	{
		return 0;
	}
				
} 
