#include<iostream>
#include<fstream>
#include<string>
#include<vector>
using namespace std;
void getSubstring(string str,vector<long> &indexPosVec,vector<long> &lengthVec,long decidedlength)
{
	char vowels[5]={'a','e','i','o','u'};
	bool isconsonant=true;
	bool previousisConsonant=true;
	long length=0;
	for(int index=0;index<str.size();index++)
	{
		previousisConsonant=isconsonant;
		bool decided=false;
		for(int judgeindex=0;judgeindex<=4;judgeindex++)
		{
			if(str[index]==vowels[judgeindex])
			{
				isconsonant=false;
				decided=true;
				break;
			}
		}
		if(decided==false)
		{
			isconsonant=true;
		}
		if(isconsonant==false)
		{
			if(previousisConsonant==true)
			{
				if(length>=decidedlength)
				{
					lengthVec.push_back(length);
					indexPosVec.push_back(index-length);
				}
			}
			length=0;
		}
		else
		{
			length++;
			if(index==str.size()-1)
			{
				if(length>=decidedlength)
				{
					lengthVec.push_back(length);
					indexPosVec.push_back(index-length+1);
				}
			}
		}
	}
}

long getTimes(string str,vector<long> indexPosVec,vector<long> lengthVec,long decidedlength)
{
	long result=0;
	for(long times1=0;times1<lengthVec.size();times1++)
	{
		long startpos=-1;
		long endpos=-1;
		for(long times2=times1-1;times2>=0;times2--)
		{
			if(lengthVec[times2]>=decidedlength)
			{
				startpos=indexPosVec[times2]+lengthVec[times2]-decidedlength+1;
				break;
			}
		}
		if(startpos==-1)
		{
			startpos=0;
		}
		endpos=str.size()-1;
		long firsttimes=indexPosVec[times1]-startpos;
		long secondtimes=endpos-(indexPosVec[times1]+lengthVec[times1])+1;
		long localfirst=firsttimes;
		long localsecond=secondtimes;
		for(long times2=decidedlength;times2<=lengthVec[times1];times2++)
		{
			result+=localfirst+1;
			localfirst++;
		}
		if(secondtimes>=0)
		{
			for(long times2=decidedlength;times2<=lengthVec[times1];times2++)
			{
				result+=localsecond;
			}
		}
		result+=firsttimes*secondtimes;
	}
	return result;
}
void main()
{
	ifstream in("small1.in",ios::in);
	ofstream out("output.txt",ios::out);
	long datanum;
	in>>datanum;
	for(int index=0;index<datanum;index++)
	{
		string str;
		long consolength;
		in>>str;
		in>>consolength;
		vector<long> indexPosVec,lengthVec;
		getSubstring(str,indexPosVec,lengthVec,consolength);
		long result=getTimes(str,indexPosVec,lengthVec,consolength);
		out<<"Case #"<<index+1<<": "<<result<<endl;
	}

}