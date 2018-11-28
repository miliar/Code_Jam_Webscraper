#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
using namespace std;

long long int hash[10];
long long int counti = 1;

int check(long long int* hash)
{
	int flag=1;
	for(int i=0;i<10;i++)
	{
		if(hash[i]==0)
			flag=0;
	}
	return flag;
}
void countsheep(long long int pass, long long int test, long long int number)
{
	long long int cpy;
	
	if(pass == 0)
	{
		
		ofstream outfile;
	  	outfile.open("Output-large.txt", std::ios_base::app);
	  	outfile << "Case #"<<test<<": INSOMNIA"<< endl;
	  	outfile.close();
	  	
	  	//cout<< "Case #"<<test<<": INSOMNIA"<< endl;
	  	return;
	}
	else
	{
		cpy = pass;
		int d;
		while(cpy!=0)
		{
			d=cpy%10;
   	        hash[d]++;
   	        cpy=cpy/10;
		}

		if(check(hash)==1)
		{
			
			ofstream outfile;
			outfile.open("Output-large.txt", std::ios_base::app);
			long long int ans = number * counti;
	  		outfile << "Case #"<<test<<": "<<ans<< endl;
	  		outfile.close();
	  		
	  		//
	  		//cout<<"Case #"<<test<<": "<< ans << endl;
	  		return;
		}
		else
		{
			counti = counti+1;
			long long int pass = number*counti;
			countsheep(pass,test,number);
		}
  	}
}

int main()
{
	long long int test, i=1, number;
	
	ifstream myfile ("A-large.txt");
	if (myfile.is_open())
  	{
  		myfile >> test;
  		while ( myfile >> number )
	    {
	      	for(long long j=0;j<10;j++)
			hash[j]=0;
	    	countsheep(number,i,number);
	    	i = i+1;
	    	counti = 0;
	    }
	    myfile.close();
	}

	/*
	cin>>test;
	while(test--)
	{
		cin>>number;
		for(long long j=0;j<10;j++)
			hash[j]=0;
	    countsheep(number,i,number);
	    i = i+1;
	    counti = 0;
	}
	*/
	return 0;
}