#include<iostream>
#include<string>
#include<fstream>
#include<vector>
#include<map>
#include<math.h>
using namespace std;
string globaldata[50000];
int smallerorEqual(string first,string second)
{
	if(first.size()<second.size())
		return -1;
	else if(first.size()>second.size())
		return 1;
	else
		return strcmp(first.c_str(),second.c_str());
}
int binarysearch(int start,int end,string globaldata[50000],string toSearch,int isFirst)
{
	if(start==end||start==end-1)
	{
		string tt=globaldata[start];
		string tt2=globaldata[end];
;		if(strcmp(globaldata[start].c_str(),toSearch.c_str())==0)
		{
			if(isFirst==1)
				return start-1;
			else
				return start;
		}
		else if(strcmp(globaldata[end].c_str(),toSearch.c_str())==0)
		{
			if(isFirst==1)
				return start;
			else
				return start+1;
		}
		else
			return start;
	}	
	else
	{
		int middle=(start+end)/2;
		if(smallerorEqual(globaldata[middle],toSearch)==-1)
		{
			return binarysearch(middle,end,globaldata,toSearch,isFirst);
		}
		else
		{
			return binarysearch(start,middle,globaldata,toSearch,isFirst);
		}
	}
}
void main()
{
	ifstream in("table.txt",ios::in);
	ifstream datain("C-large-2.in",ios::out);
	ofstream out("finaloutput.txt",ios::out);
	int numofData=0;
	while(!in.eof())
	{
		string data;
		in>>data;
		globaldata[numofData]=data;
		numofData++;
	}
	int times;
	datain>>times;
	for(int index=1;index<=times;index++)
	{
		cout<<index<<endl;
		string first,second;
		datain>>first>>second;
		int firstindex=binarysearch(0,numofData-1,globaldata,first,1);
		int secondindex=binarysearch(0,numofData-1,globaldata,second,2);
		out<<"Case #"<<index<<": "<<secondindex-firstindex<<endl;
	}
}