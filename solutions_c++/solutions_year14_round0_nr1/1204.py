
#include<iostream>
#include<fstream>
#include<vector>
#include<time.h>
using namespace std;

int main()
{
	int start=clock();
 
	fstream input;
	input.open("A-small-attempt.in");
    ofstream out("a-small.txt"); 
	
	int n;//number of test case n
	input>>n;

	for(int i=0;i<n;i++)
	{
	
		int answer1=0;
		int answer2=0;
	
		int hash[17];
		memset(hash,0,17*sizeof(int));
		//int cards[4][4];
		input>>answer1;
		vector<int> rowFirst;
		for(int m=0;m<4;m++)
		{
			for(int n=0;n<4;n++)
			{
				int temp=0;
				input>>temp;
				if(answer1==m+1)
				{
					rowFirst.push_back(temp);
					hash[temp]=1;
				}
			}
		}

		//second answer
		input>>answer2;
		vector<int> rowSecond;
		for( m=0;m<4;m++)
		{
			for(int n=0;n<4;n++)
			{
				int temp=0;
				input>>temp;
				if(answer2==m+1)
				{
					rowSecond.push_back(temp);
				}
			}
		}
	    
		int count=0;
		int result=0;
		for(int l=0;l<rowSecond.size();l++)
		{
			if(hash[rowSecond[l]])
			{
				count++;
				result=rowSecond[l];
			}
		}
		if(1==count)
		{
			out<<"Case #"<<i+1<<": "<<result<<endl;
		}
		else if(count==0)
		{
			out<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
		}
		else
		{
		    out<<"Case #"<<i+1<<": Bad magician!"<<endl;
		}

	}
	input.close();
	out.close();
    int end=clock();
	cout<<"the total time of running is :"<<end-start<<endl;
	return 0;
}