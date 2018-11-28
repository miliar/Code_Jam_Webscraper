#include <iostream>
#include <fstream>
#include <string>

using namespace std;
int main()
{
	unsigned int test_case;
	unsigned int str_len,friends=0;
	string str;
	ifstream myfile;
	myfile.open("A-small-attempt1");
	myfile>>test_case;
	ofstream out;
	out.open("outup_A.txt");
	int j;
		
	for(int i=1;i<=test_case;i++)
	{   
		friends=0;
		myfile>>str_len;
		j=0;
		myfile>>str;
		for (int i=1; i<=str_len; i++)
    	{
    		j=j+str[i-1]-48;  //_48 becUSE CHAR WILL GIVE ASCII VALUE
		    if(j<i)
     		{ 
     			friends++;
     			j++;
     		}
     }
     	out<<"case #"<<i<<"  " <<friends<<endl;
   }
     
     myfile.close();
     return 0;
}
