#include <iostream>
#include <fstream>
#include <string>
using namespace std;
#ifdef TEST
#undef TEST
#endif

//#define TEST

const int TRANS_IJK[4][4]={
	{0,1,2,3},
	{1,0,3,2},
	{2,3,0,1},
	{3,2,1,0}
	};
//0~1,1~i,2~j,3~k
const int TRANS_SGN[4][4]={
	{0,0,0,0},
	{0,1,0,1},
	{0,1,1,0},
	{0,0,1,1},
	};
//0~positive,1~negative

int compute(string s)
//compute the string S with only character i,j,k, 
//return value stands for:
//0~1,1~i,2~j,3~k,4~-1,5~-i,6~-j,7~-k;
{
	int value=0;
	int sgn=0;
	int mul;
	for(int i=0;i<s.length();++i)
	{
		if(s[i]=='i') mul=1;
		else if(s[i]=='j') mul=2;
		else if(s[i]=='k') mul=3;
		else {mul=0;cerr<<"Invalid Input s!"<<endl;}
		
		sgn = (TRANS_SGN[value][mul] + sgn) %2;
		value = TRANS_IJK[value][mul];
	}
	return value + sgn*4;
}	


int main(int argc, char** argv)
{
	//compute all the possible substring start from the beginning and the following
	//  if find an "i", we've done the first part
    //  if find an "ij=k" then, we've done the second part
	//if the whole is just -1, then we've get it.

#ifdef TEST
	istream &input = cin;
	ostream &output = cout;
#else
	ifstream input("in.txt",ios_base::in);
	ofstream output("out.txt",ios_base::out);
#endif
	
	int T;
	input>>T;
	for(int x=1;x<=T;++x)
	{
		int L,X;
		input>>L>>X;
		string s;
		input>>s;
		
		bool findi=false;
		bool findij=false;
		int value=0;
		int sgn=0;
		int i=0;//index of s
		int j=0;//index among the X 
		while(j<X)
		{
			int mul;
			if(s[i]=='i') mul=1;
			else if(s[i]=='j') mul=2;
			else if(s[i]=='k') mul=3;
			else {mul=0;cerr<<"Invalid Input s!"<<endl;}
			
			sgn = (TRANS_SGN[value][mul] + sgn) %2;
			value = TRANS_IJK[value][mul];
			//cout<<i<<','<<j<<' '<<sgn*4+value<<endl;
			
			if(!findi)
			{
				if(value==1 && sgn==0)
					findi=true;
			}
			else if(!findij)
			{
				if(value==3 && sgn==0)
					findij=true;
			}
			
			++i;
			if(i==L)
			{
				i=0;++j;
			}
		}
		if(findij && value==0 && sgn==1)
			output<<"Case #"<<x<<": YES"<<endl;
		else
			output<<"Case #"<<x<<": NO"<<endl;
	}
#ifndef TEST
	output.close();
	input.close();
#endif
	return 0;
}