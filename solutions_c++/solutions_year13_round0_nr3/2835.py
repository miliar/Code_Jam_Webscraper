//2013 GCJ Qualification round Problem C. Fair and Square
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>
#include<math.h>
using namespace std;

bool is_nth_power(int a, int n) {
 
    int b = pow(a, 1. / n);
  return pow( (double)b, n) == a ;
}

bool is_palidrome(string str)
{
int x = str.length()-1;

for(int i = 0; i <= x; i++)
{
	if (str[i] == str[x-i])
	{
		continue;
	}
	else
	{
		//cout<<"Not a palidrome"<<endl;
		return false;
	}
}

	//cout << "Indeed Palidrome"<<endl;
	return true;

}

int check(int a,int b)
{
	int num=0;
	
	for (int i=a;i<=b;i++)
	{
		
		ostringstream ss;
       ss << i;
      string I= ss.str();
	  
		//itoa(i,I,10);
		
		//std::string s = std::to_string(i);
		if (I[0]==I[I.length()-1] && (I[0]=='1'||I[0]=='4'||I[0]=='5'||I[0]=='6'||I[0]=='9'))
		{
			
		
			if (is_nth_power(i,2))
			{
				int b=pow(i,1./2);
			
				ostringstream ssb;
				ssb << b;
				string Ib= ssb.str();
					cout<<Ib<<endl;
				if (is_palidrome(I) && is_palidrome(Ib) )
					{
						cout<<I<<endl;
						num++;
						
			         }
			}
		}

		else
			{

			continue;}
		
	}	



	return num;
}




int main()
{   
	

	ifstream fin("C-small-attempt0.in");
	//ifstream fin("C-small-attempt0.in");
	//ifstream fin("C-large.in");
	int T;
	fin>>T;
	//cout<<T;
	//ofstream fout("C.out");
	ofstream fout("C-small-attempt0.out");
	//ofstream fout("C-large.out");	
	
	
	//int A,B;

	//char* A=new char[4];
    //char* B=new char[4];
	


	for (int n=1;n<=T;n++)
	{
		
		//char* A=new char[4];
		//char* B=new char[4];

		int A,B;
		fin>>A>>B;
		
			
			
		int  num=check(A,B);
	    	
		fout<<"Case #"<<n<<": ";
	
		fout<<num<<endl;

		//delete []A;
	   // delete []B;
		
	}
	
	
	
	return 0;
}