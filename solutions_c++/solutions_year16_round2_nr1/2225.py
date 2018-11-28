#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
using namespace std;

void find(string& s, int test)
{
	ofstream outfile;

  	outfile.open("output.txt", std::ios_base::app);
	outfile << "Case #"<<test<<": ";
	int freq[26] = {0};
	int len = s.length();
	int k=0;
	for(int i=0;i<len;i++)
	{
		freq[s[i]-65]++;
	}
	int num[700];
	while(freq[25]>0)
	{
		freq[4]--;
		freq[17]--;
		freq[14]--;
		freq[25]--;
		num[k++]=0;
	}
	while(freq[23]>0)
	{
		freq[18]--;
		freq[8]--;
		freq[23]--;
		num[k++]=6;
	}
	while(freq[18]>0)
	{
		freq[18]--;
		freq[4]--;
		freq[4]--;
		freq[21]--;
		freq[13]--;
		num[k++]=7;
	}
	while(freq[21]>0)
	{
		freq[21]--;
		freq[5]--;
		freq[4]--;
		freq[8]--;
		num[k++]=5;
	}
	while(freq[5]>0)
	{
		freq[14]--;
		freq[5]--;
		freq[20]--;
		freq[17]--;
		num[k++]=4;
	}
	while(freq[17]>0)
	{
		freq[17]--;
		freq[4]--;
		freq[4]--;
		freq[19]--;
		freq[7]--;
		num[k++]=3;
	}
	while(freq[7]>0)
	{
		freq[7]--;
		freq[4]--;
		freq[6]--;
		freq[19]--;
		freq[8]--;
		num[k++]=8;
	}
	while(freq[22]>0)
	{
		freq[22]--;
		freq[19]--;
		freq[14]--;
		num[k++]=2;
	}
	while(freq[8]>0)
	{
		freq[9]--;
		freq[9]--;
		freq[8]--;
		freq[4]--;
		num[k++]=9;
	}
	while(freq[14]>0)
	{
		freq[14]--;
		freq[13]--;
		freq[4]--;
		num[k++]=1;
	}
	sort(num,num+k);
	for(int i=0;i<k;i++)
	{
		outfile << num[i];
	}
	outfile << endl;
}
int main()
{
	long long int test, i=0;
	ifstream myfile ("b.txt");
	if (myfile.is_open())
  	{
  		myfile >> test;
  		string line;
	    while ( getline (myfile,line) )
	    {
	      find(line,i);
	      i = i+1;
	    }
	    myfile.close();
  	}
	return 0;
}