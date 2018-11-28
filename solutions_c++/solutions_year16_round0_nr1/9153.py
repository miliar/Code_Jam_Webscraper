#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string>
#include<string.h>
#include<sstream>
#include<ostream>
#include<fstream>
using namespace std;
int str_to_int(string strip)
{
	int num=0,c,dec=1;
	c = strip.length()-1;
	//cout << strip.at(strip.length()-1) << endl;
	while(c != -1)
	{
		num+=dec*(strip.at(c)-48);
		c--;
		dec*=10;
	}
	return num;	
}
int main()
{
	int test,k=0;
	string line;
	ifstream my_file("A-large.in");
	ofstream my_file_2("output.in");
	ostringstream oss;
	if (my_file.is_open())
	{	
		getline(my_file,line);
		test = str_to_int(line);
//		cout << test << endl ;
	}
	//scanf("%d",&test);
		while(getline(my_file,line))
		{
			k = k+1	;		
		int num,arr[10]={0};
		num = str_to_int(line);
		//scanf("%d",&num);
		if (num == 0)
		{
			if(my_file_2.is_open())
			{
				oss << "Case #" << k << ": INSOMNIA\n" ;
				//my_file_2 << oss.str();
			}
		}
		else 
		{
			int temp;
			int i;
			for(i=1;;i++)
			{
				temp = num*i;
				while(temp > 0)
				{	
					int x;
					x=temp%10;
					if (arr[x]!=1)
					{
						arr[x]=1;
					}
					temp=temp/10;
				}
				int sum = 0;
				for(int j=0;j<10;j++)
				{	
					sum+=arr[j];
				}
				if(sum==10)
				{
					if(my_file_2.is_open())
					{	
						oss << "Case #"<< k <<": " << i*num << endl;
					//	my_file_2 << oss.str();
					}
					break;
				}	
			}	
		}
		
		}
		my_file_2 << oss.str();
		my_file_2.close();
		my_file.close();
		
	return 0;	
}
