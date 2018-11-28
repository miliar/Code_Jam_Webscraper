#include<iostream>
#include<string>
#include<sstream>
#include<fstream>
using namespace std;


int main()
{
	int numcases;
	string shynessstring;
	ifstream myfile;
	myfile.open("input.txt");
	myfile>>numcases;
	//getline(cin,line);
	int maxshyness,myfriends,numstanding;
	for(int i = 0 ; i < numcases ; i++)
	{
		numstanding = 0 ; myfriends = 0;

		
		//stringstream ss(line);
		myfile>>maxshyness;
		myfile>>shynessstring;
		for(int j = 0 ; j <= shynessstring.size() ; j++)
		{
			if(j<=numstanding+myfriends)
			{
				numstanding = numstanding+shynessstring[j]-'0';
			}else
			{
				myfriends = myfriends + j - numstanding - myfriends ;
				numstanding = numstanding + shynessstring[j]-'0';
			}	
		}
		cout<<"Case #"<<i+1<<": "<<myfriends<<endl;

	}
	myfile.close();
		
}
