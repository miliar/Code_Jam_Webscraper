#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
using namespace std;

int main(int argc, char** argv)
{
	ifstream myfile;
	myfile.open(argv[1]);
	int num_test;
	myfile>>num_test;
	
	for (int num=0;num<num_test;num++)
	{
		int a;
		
		myfile>>a;
		
		
    	int firstr[4];
    	for (int j=0;j<5;j++)
   		{
  			string row;
   			getline(myfile,row);
   			if (j==a)
    		{
    			stringstream stream(row);
   				for (int k=0;k<4;k++)
   				{
   					stream>>firstr[k];
   				}
   			}
    	}
    	
    	int b;
    	
    	myfile>>b;
    	
    	int secondr[4];
   		for (int m=0; m<5; m++)
   		{
   			string row;
   			getline(myfile,row);
   			if(m==b)
    		{
   				stringstream stream(row);
   				for (int n=0;n<4;n++)
   				{
   					stream>>secondr[n];
     			}
    			
    		}
    	}
    	int num_of_same=0;
    	int answer;
    	for (int f=0;f<4;f++)
    	{
    		for (int g=0;g<4;g++)
    	    {
    			if (firstr[f]==secondr[g])
    			{
    				num_of_same++;
    				answer=firstr[f];
    			}
    		}

    	}
    	if (num_of_same >1)
    	{
    		cout<<"Case #"<<num+1<<": Bad magician!"<<endl;

    	}
    	else if (num_of_same==1)
    	{
    		cout<<"Case #"<<num+1<<": "<<answer<<endl;;

    	}
    	else
    	{
    		cout<<"Case #"<<num+1<<": Volunteer cheated!"<<endl;
    	}
    	
	}
    

	

}