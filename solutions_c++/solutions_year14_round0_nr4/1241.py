
#include<iostream>
#include<fstream>
#include<vector>
#include<time.h>
#include<algorithm>
using namespace std;

vector<int> Game(vector<double> &first,vector<double> &second)
{
	vector<int> result;
	sort(first.begin(),first.end());
	sort(second.begin(),second.end());
	int length=first.size();
	int countofDec=0;
	int countofWar=0;
	if(first[0]>second[length-1])
	{
		result.push_back(length);
		result.push_back(length);
		return result;
	}
	if(first[length-1]<second[0])
	{
		result.push_back(0);
		result.push_back(0);
		return result;
	}
	int i=length-1;
	int j=length-1;
	while(i>=0&&j>=0)
	{
		if(first[i]>second[j])
		{
			countofDec++;
			i--;
			j--;
		}
		else
		{
			j--;
		}
	}

	i=length-1;
	j=length-1;
	int temp=0;
	while(i>=0&&j>=0)
	{
		if(second[j]>first[i])
		{
			temp++;
			i--;
			j--;
		}
		else
		{
			i--;
		}
	}
	countofWar=length-temp;
	result.push_back(countofDec);
	result.push_back(countofWar);
	return result;
}

int main()
{
	int start=clock();
	
	fstream input;
	input.open("D-large-attempt.in");
    ofstream out("d-large.txt"); 
	
	int n;//number of test case n
	input>>n;

	for(int i=0;i<n;i++)
	{
		int numberofblock=0;
		input>>numberofblock;
		vector<double> first;
		vector<double> second;
		for(int j=0;j<numberofblock;j++)
		{
			double temp;
			input>>temp;
			first.push_back(temp);
		}
		for( j=0;j<numberofblock;j++)
		{
			double temp;
			input>>temp;
			second.push_back(temp);
		}
		vector<int> result;
		result=Game(first,second);

	

		out<<"Case #"<<i+1<<": "<<result[0]<<" "<<result[1]<<endl;

	}
	input.close();
	out.close();
    int end=clock();
	cout<<"the total time of running is :"<<end-start<<endl;
	return 0;
}