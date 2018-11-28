#include<iostream>
#include<fstream>
#include<vector>
#include<time.h>
#include<algorithm>
#include<stack>

#include <sstream> 
#include <string>
using namespace std;

int Game(vector<string> &vec)
{
	int length=vec.size();
	int hash[256];
	memset(hash,0,sizeof(int)*256);
	
	for(int i=0;i<length;i++)
	{
		for(int j=0;j<vec[i].size();j++)
			hash[vec[i][j]]++;
	}
	for( i=0;i<256;i++)
	{
		if(hash[i]==1)
			return -1;
	}
	int lengthoffirst=vec[0].size();
	int lengthofSecond=vec[1].size();
	int m=0;
	int n=0;
	int count=0;
	while(m<lengthoffirst&&n<lengthofSecond)
	{
		if(vec[0][m]==vec[1][n])
		{
			m++;
			n++;
		}
		else
		{
			if((m==0)||(n==0))
				return -1;
			if(vec[0][m]==vec[0][m-1])
			{
				count++;
				m++;
			}
			else if(vec[1][n]==vec[1][n-1])
			{
				count++;
				n++;
			}
			else
				return -1;
		
		}
	}
	while(m<lengthoffirst)
	{
		if(vec[0][m]==vec[0][m-1])
		{
			count++;
			m++;
		}
		else
			return -1;
	}
	while(n<lengthofSecond)
	{
		if(vec[1][n]==vec[1][n-1])
		{
			count++;
			n++;
		}
		else
			return -1;
	}
	
	return count;
}
int main()
{
	int start=clock();
 
	fstream input;
	input.open("A-small-attempt4.in");
	//input.open("3.txt");
    ofstream out("a-small.txt"); 
	
	int n;//number of test case n
	input>>n;

	for(int i=0;i<n;i++)
	{
	
		int numofstrings=0;
		
		input>>numofstrings;
		vector<string> vec;
		char ch;
		input.get(ch);

	//	for(int m=0;m<numofstrings;m++)
	//	{
			
			string temp="";
			int numofword=0;
			while(input.get(ch))
			{
		      if(ch!='\n')
				temp=temp + ch;	
		      else
			  {
				numofword++;
				vec.push_back(temp);
				temp="";
				if(numofword==numofstrings)
					break;
			  }
			}
			if(temp!="")
				vec.push_back(temp);
			
	//	}
	

		//second answer
		int count =Game(vec) ;
	
		if(count!=-1)
		{
			out<<"Case #"<<i+1<<": "<<count<<endl;
		}
		else
		{
		    out<<"Case #"<<i+1<<": Fegla Won"<<endl;
		}

	}
	input.close();
	out.close();
    int end=clock();
	cout<<"the total time of running is :"<<end-start<<endl;
	return 0;
}